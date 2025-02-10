import { 
    fetchStaticData, 
    getEmptyCharacter, 
    getCookie, 
    switchObjectNamingConventions,
    editingContexts
} from "./utils.js";
import { showToast } from './toast.js';


document.addEventListener("alpine:init", () => {
    Alpine.prefix("data-");
    Alpine.data('characterGenerator', () => ({
        character: null,
        staticData: null,
        isLoading: true,
        currentPage: "race",
        editingContext: null,
        characterId: null,
        // Just tracks whether the user has switched pages, so always true
        // after the first switch.
        pageSwitchMade: false,
        isGeneratingImage: false,
        isUploadingImage: false,
        cropperInstance: null,
        enableImageGeneration: false,

        /**
         * Initialise the component by fetching the static data and setting the initial state.
         */
        async init() {
            try {
                this.isLoading = true;
                this.staticData = await fetchStaticData();
                this.setInitialState();
                this.initialiseCroppingButtons();
                this.isLoading = false;
            } catch (error) {
                console.error('Error fetching JSON:', error);
                showToast("Failed to load character generator, please try again later.");
            }
        },
        /**
         * Set the initial state of the character generator, based on the data passed in from the server.
         */
        setInitialState() {
            if (window.editorData) {
                const { editingContext, characterData, characterId, enableImageGeneration } = window.editorData;
                this.editingContext = editingContext;
                this.characterId = characterId;
                this.enableImageGeneration = enableImageGeneration;
                if (editingContext === editingContexts.editExisting || editingContext === editingContexts.cloneExisting) {
                    this.character = switchObjectNamingConventions(characterData);
                } else {
                    this.character = getEmptyCharacter();
                }
            }
        },
        /**
         * Initialise the buttons for the image cropping tool, adding event listeners to them.
         */
        initialiseCroppingButtons() {
            const cropImageButton = document.getElementById('crop-image-button');
            const cropCancelButton = document.getElementById('crop-cancel-button');
            const imageModalOverlay = document.getElementById('image-modal-overlay');
            // On click, retrieve cropped image from cropper instance, convert to blob, and POST to server.
            cropImageButton.addEventListener('click', () => {
                if (this.cropperInstance) {
                    const data = this.cropperInstance.getData();
                    const croppedWidth = Math.min(data.width, 500);
                    this.isUploadingImage = true;
                    this.cropperInstance.getCroppedCanvas({ width: croppedWidth }).toBlob(async (blob) => {
                        const formData = new FormData();
                        formData.append('image', blob);
                        const csrfToken = getCookie('csrftoken');
                        const url = `/characters/upload-image/`;
                        try {
                            const response = await fetch(url, {
                                method: 'POST',
                                headers: {
                                    'X-CSRFToken': csrfToken
                                },
                                body: formData
                            });
                            if (!response.ok) {
                                throw new Error('Failed to POST image');
                            }
                            const data = await response.json();
                            this.character.image = {
                                url: data.url,
                                id: data.id
                            }
                            imageModalOverlay.style.display = 'none';
                            this.isUploadingImage = false;
                        } catch (error) {
                            console.error('Error POSTing image:', error);
                            showToast("Failed to upload image, please try again later.");
                        }
                    })
                }
            });
            // On click, destroy the cropper instance and hide the modal.
            cropCancelButton.addEventListener('click', () => {
                if (this.cropperInstance) {
                    this.cropperInstance.destroy();
                }
                imageModalOverlay.style.display = 'none';
            });
        },
        /**
         * Switch to the given page by updating the currentPage variable, and ensures that
         * the pageSwitchMade variable is set to true.
         * @param {string} page The page to switch to.
         */
        setPage(page) {
            this.currentPage = page;
            this.pageSwitchMade = true;
        },
        /**
         * Encapsulates the logic for moving to the next page based on the
         * current page and the editor state.
         */
        moveToNextPage() {
            switch (this.currentPage) {
                case 'race':
                    this.setPage('class');
                    break;
                case 'class':
                    this.setPage('abilityPoints');
                    break;
                case 'abilityPoints':
                    this.isCaster ? this.setPage('spells') : this.setPage('background');
                    break;
                case 'spells':
                    this.setPage('background');
                    break;
                case 'background':
                    this.setPage('appearance');
                    break;
                case 'appearance':
                    this.setPage('finalise');
                    break;
                default:
                    console.error("Invalid page name");
            }
        },
        /**
         * Return the static data for the race that has been chosen by the user.
         */
        get chosenRace() {
            return this.staticData.races.find(r => r.id === this.character.race);
        },
        /**
         * Return the static data for the class that has been chosen by the user.
         */
        get chosenClass() {
            return this.staticData.classes.find(c => c.id === this.character.class);
        },
        /**
         * Computes the number of skill proficiencies that the user can choose, based on
         * their choice of class and race.
         */
        get computedNumberOfSkillProficiencies() {
            const classSkillProficiencies = this.chosenClass ? this.chosenClass.proficiencies.skills.choose : 0;
            const raceSkillProficiencies = this.chosenRace ? this.chosenRace.additionalSkillProficiencies : 0;
            return classSkillProficiencies + raceSkillProficiencies;
        },
        /**
         * Returns true if the chosen class has a spellcasting ability, false otherwise.
         */
        get isCaster() {
            return this.chosenClass.spellcasting.ability !== null;
        },
        /**
         * Returns true if the race portion of the character creation is complete, false otherwise.
         */
        get raceIsComplete() {
            // With the current design, it is impossible for race to be incomplete, but for 
            // consistency with other pages, we will add a check for it.
            return true;
        },
        /**
         * Returns true if the class portion of the character creation is complete, false otherwise.
         */
        get classIsComplete() {
            return this.character.classSkillChoices.length === this.computedNumberOfSkillProficiencies;
        },
        /**
         * Returns true if the ability points portion of the character creation is complete, false otherwise.
         */
        get abilityPointsIsComplete() {
            for (let i = 0; i < this.character.abilityPoints.length; i++) {
                if (this.character.abilityPoints[i].value === "--") {
                    return false;
                }
            }
            return true;
        },
        /**
         * Returns true if the spells portion of the character creation is complete or the
         * character is not a spellcaster, otherwise returns false.
         */
        get spellsIsComplete() {
            if (this.isCaster) {
                if (this.character.classCantripChoices.length !== this.chosenClass.spellcasting.cantrips.choose) {
                    return false;
                }
                if (this.character.classSpellChoices.length !== this.chosenClass.spellcasting.spells.choose) {
                    return false;
                }
            }
            return true;
        },
        /**
         * Returns true if the background portion of the character creation is complete, false otherwise.
         */
        get backgroundIsComplete() {
            return (Boolean(this.character.name.trim()) && Boolean(this.character.age) && 
                    Boolean(this.character.gender.trim()) && Boolean(this.character.background.trim())
                )
        },
        /**
         * Returns true if the appearance portion of the character creation is complete, false otherwise.
         */
        get appearanceIsComplete() {
            return (Boolean(this.character.height.trim()) && Boolean(this.character.build.trim()) && 
                    Boolean(this.character.skinTone.trim()) && Boolean(this.character.eyeColor.trim()) && 
                    Boolean(this.character.hairColor.trim()) && Boolean(this.character.hairStyle.trim()) && 
                    Boolean(this.character.clothingStyle.trim()) && Boolean(this.character.clothingColors.trim())
                )
        },
        /**
         * Returns true if all portions of the character creation are complete, false otherwise.
         */
        get isComplete() {
            return (this.raceIsComplete && this.classIsComplete && this.abilityPointsIsComplete &&
                this.spellsIsComplete && this.backgroundIsComplete && this.appearanceIsComplete
            );
        },
        /**
         * Get the current base score for the given ability, with no bonuses applied.
         * @param {string} abilityId - the id of the ability to get the base score for.
         * @returns 
         */
        getAbilityBaseScore(abilityId) {
            const ability = this.character.abilityPoints.find(a => a.id === abilityId);
            return ability.value;
        },
        /**
         * Get the racial ability bonus for the given ability.
         * @param {string} abilityId - the id of the ability to get the bonus for.
         * @returns 
         */
        getRacialAbilityBonus(abilityId) {
            const bonus = this.chosenRace.abilityBonuses.find(a => a.ability.id === abilityId);
            return bonus.bonus;
        },
        /**
         * Get the adjusted ability score for the given ability, with racial bonuses applied.
         * @param {string} abilityId - the id of the ability to get the adjusted score for.
         * @returns 
         */
        getAdjustedAbilityScore(abilityId) {
            const baseScore = this.getAbilityBaseScore(abilityId);
            const racialBonus = this.getRacialAbilityBonus(abilityId);
            if (baseScore === "--") {
                return "--";
            } else {
                return baseScore + racialBonus;
            }
        },
        /**
         * Get the modifier for the given ability (adjusted).
         * @param {string} abilityId - the id of the ability to get the modifier for.
         * @returns 
         */
        getAbilityModifier(abilityId) {
            const score = this.getAdjustedAbilityScore(abilityId);
            // If the score is '--', then the modifier is 0, regardless of racial bonuses.
            if (score === "--") {
                return 0;
            }
            // Otherwise, the modifier is calculated as normal.
            return Math.floor((score - 10) / 2);
        },
        /**
         * Adds or removes the given skillId from the classSkillChoices array. Respects the
         * computedNumberOfSkillProficiencies, removing the oldest skill if the user tries to
         * add more than the allowed number.
         * @param {string} skillId - the id of the skill to toggle proficiency for.
         */
        toggleSkillProficiency(skillId) {
            // Note: The full behaviour of this function is not currently utilised, as the UI
            // prevents the user from selecting any additional skills once the maximum number
            // has been reached. However, for robustness, the function has been left as is.
            const index = this.character.classSkillChoices.indexOf(skillId);
            // If the skill is not already in the array...
            if (index === -1) {
                // ... then add it to the array, if there is space.
                if (this.character.classSkillChoices.length < this.computedNumberOfSkillProficiencies) {
                    this.character.classSkillChoices.push(skillId);
                // If there is not space, then remove the first (oldest) skill from the array,
                // and add the new one at the end
                } else {
                    this.character.classSkillChoices.shift();
                    this.character.classSkillChoices.push(skillId);
                }
            // If the skill is already in the array, remove it.
            } else {
                this.character.classSkillChoices.splice(index, 1); 
            }
        },
        /**
         * Return the static data for the ability with the given id
         * @param {string} abilityId - the id of the ability to get the data for.
         * @returns 
         */
        getAbilityData(abilityId) {
            return this.staticData.abilities.find(a => a.id === abilityId);
        },
        /**
         * Computes the ability point options for the given abilityId, based on which
         * points from the standard array have already been chosen.
         * @param {string} abilityId 
         * @returns 
         */
        computeAbilityPointOptions(abilityId) {
            // Construct an array containing some subset of the options
            // '--', 8, 10, 12, 13, 14, 15,
            // where '--' represents none/unset.
            // Specifically, it should include '--', the current value of this ability,
            // and any other value that has not been chosen yet.
            const currentAbilityValue = this.character.abilityPoints.find(a => a.id === abilityId).value;
            const points = [8, 10, 12, 13, 14, 15].filter(p => {
                // If the point is the current abilities value, or if there is no ability with that value,
                // then include it in the list. 
                return p === currentAbilityValue || !this.character.abilityPoints.find(a => a.value === p);
            });
            // Ensure that the none/unset option is always at the start of the list.
            points.unshift("--");
            return points;
        },
        /**
         * Resets/unsets the ability points.
         */
        resetAbilityPoints() {
            this.character.abilityPoints = this.character.abilityPoints.map(a => {
                return {
                    ...a,
                    value: "--"
                }
            });
        },
        /**
         * Sets the ability points to recommended values for the currently chosen
         * class. 
         */
        setAbilityPointsToChosenClassDefaults() {
            const classDefaults = this.chosenClass.abilities;
            for (let i = 0; i < this.character.abilityPoints.length; i++) {
                this.character.abilityPoints[i].value = classDefaults[i].value;
            }
        },
        /**
         * Perform any necessary cleanup when the race is changed.
         */
        resetStateOnRaceChange() {
            this.character.classSkillChoices = [];
        },
        /**
         * Perform any necessary cleanup when the class is changed.
         */
        resetStateOnClassChange() {
            this.character.classSkillChoices = [];
            this.character.classCantripChoices = [];
            this.character.classSpellChoices = [];
        },
        /**
         * Add the given cantrip to the list of class cantrip choices, if it is not already in the list
         * and there is space for it.
         * @param {string} cantripId - the id of the cantrip to add.
         * @returns 
         */
        addCantrip(cantripId) {
            // If the cantrip is already in the list, do nothing.
            if (this.character.classCantripChoices.includes(cantripId)) {
                console.error("Attempted to add a cantrip that is already in the list.");
                return;
            }
            // If the list is already at the maximum length, do nothing.
            if (this.character.classCantripChoices.length >= this.chosenClass.spellcasting.cantrips.choose) {
                console.error("Attempted to add more cantrips than allowed.");
                return;
            }
            this.character.classCantripChoices.push(cantripId);
        },
        /**
         * Remove the given cantrip from the list of class cantrip choices, if it is in the list.
         * @param {string} cantripId - the id of the cantrip to remove. 
         * @returns 
         */
        removeCantrip(cantripId) {
            // If the cantrip is not in the list, do nothing.
            if (!this.character.classCantripChoices.includes(cantripId)) {
                console.error("Attempted to remove a cantrip that is not in the list.");
                return;
            }
            this.character.classCantripChoices = this.character.classCantripChoices.filter(c => c !== cantripId);
        },
        /**
         * Get the static data for the cantrip with the given id.
         * @param {string} cantripId - the id of the cantrip to get the data for. 
         * @returns 
         */
        getCantripData(cantripId) {
            return this.staticData.spells.find(c => c.id === cantripId);
        },
        /**
         * Add the given spell to the list of class spell choices, if it is not already in the list
         * and there is space for it.
         * @param {string} spellId - the id of the spell to add.
         * @returns 
         */
        addSpell(spellId) {
            // If the spell is already in the list, do nothing.
            if (this.character.classSpellChoices.includes(spellId)) {
                console.error("Attempted to add a spell that is already in the list.");
                return;
            }
            // If the list is already at the maximum length, do nothing.
            if (this.character.classSpellChoices.length >= this.chosenClass.spellcasting.spells.choose) {
                console.error("Attempted to add more spells than allowed.");
                return;
            }
            this.character.classSpellChoices.push(spellId);
        },
        /**
         * Remove the given spell from the list of class spell choices, if it is in the list.
         * @param {string} spellId - the id of the spell to remove.
         * @returns 
         */
        removeSpell(spellId) {
            // If the spell is not in the list, do nothing.
            if (!this.character.classSpellChoices.includes(spellId)) {
                console.error("Attempted to remove a cantrip that is not in the list.");
                return;
            }
            this.character.classSpellChoices = this.character.classSpellChoices.filter(s => s !== spellId);
        },
        /**
         * Get the static data for the spell with the given id.
         * @param {string} spellId - the id of the spell to get the data for. 
         * @returns 
         */
        getSpellData(spellId) {
            return this.staticData.spells.find(s => s.id === spellId);
        },
        /**
         * Adjust facial hair length value to account for whether the character has facial hair or not.
         * Attached to the change event of the facial hair style select element.
         * @param {*} e 
         */
        adjustFacialHairLength(e) {
            const newStyle = e.target.value;
            // If the new style is None or Stubble, then the length should be an empty string.
            if (newStyle === "None" || newStyle === "Stubble") {
                this.character.facialHairLength = "";
            // If the new style is not None or Stubble, and the length is an empty string, 
            // then set it to Short, but don't overwrite if it is already set to something else.
            } else if (this.character.facialHairLength === "") {
                this.character.facialHairLength = "Short";
            }
        },
        /**
         * Replaces line breaks in the given text with <br> tags, which will be respected by HTML.
         * @param {string} text - the text to format. 
         * @returns 
         */
        formatLineBreaks(text) {
            return text.replace(/(?:\r\n|\r|\n)/g, '<br/>');
        },
        /**
         * When the user has finished creating their character, POST the character to the server.
         */
        async handleSubmit(e) {
            e.preventDefault();
            // Get the CSRF token from the cookie.
            const csrfToken = getCookie('csrftoken');
            // Format the character object to match the Python naming conventions.
            const python_ready_character = switchObjectNamingConventions(this.character);
            // The character editor stores both the image url and public id, but the backend
            // only cares about the public id, so we can overwrite the image object with just the id.
            python_ready_character.image = python_ready_character.image.id;
            if (python_ready_character.facial_hair_length === "") {
                python_ready_character.facial_hair_length = null;
            }
            let url = '';
            // Set the URL to POST to based on the editing context.
            if (this.editingContext === editingContexts.editExisting) {
                url = `/characters/${this.characterId}/edit/`;
            } else {
                url = '/characters/new/';
            }
            // Try to POST the character to the server.
            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify(python_ready_character)
                });
                if (!response.ok) {
                    throw new Error('Failed to POST character');
                }
                const data = await response.json();
                // Redirect to the correct character sheet page. If the character was just created, 
                // then we have to get the characterId from the response data.
                if (this.editingContext === editingContexts.createNew || 
                    this.editingContext === editingContexts.cloneExisting) {
                        this.characterId = data.characterId;
                }
                window.location.href = `/characters/${this.characterId}/`;
            } catch (error) {
                // Handle any errors that occur during the POST request by alerting
                // to the console and showing a toast message to the user.
                console.error('Error POSTing character:', error);
                showToast("Failed to save character, please try again.");
            }
        },
        /**
         * Grabs the image file that the user selected, performs some maths to scale it correctly to the viewport,
         * and then creates a Cropper instance with the image.
         * @param {*} e 
         */
        openCropTool(e) {
            // Get the file that the user selected.
            const file = e.target.files[0];
            if (file) {
                // Create a FileReader to read the file as a data URL.
                // Whn the file is loaded, display the image and create
                // a Cropper instance.
                const reader = new FileReader();
                reader.onload = (e) => {
                    const imageModalOverlay = document.getElementById('image-modal-overlay');
        
                    imageModalOverlay.style.display = 'flex';
                    const imageCropContainer = document.getElementById('image-crop-container');
                    const imageToCrop = document.getElementById('image-to-crop');
                    imageToCrop.src = e.target.result;
                    imageToCrop.onload = () => {
                        // Perform some maths to scale the image to fit the viewport.
                        // The image should be as big as possible, but neither its width 
                        // nor height should exceed 75% of the relevant viewport measurement
                        // (innerWidth, innerHeight).
                        const naturalWidth = imageToCrop.naturalWidth;
                        const naturalHeight = imageToCrop.naturalHeight;
                        const viewportWidth = window.innerWidth;
                        const viewportHeight = window.innerHeight;
                        // Calculate the scale factors required to make the image
                        // fit in terms of width and height.
                        const xScale = (viewportWidth * 0.75) / naturalWidth;
                        const yScale = (viewportHeight * 0.75) / naturalHeight;
                        // Determine the appropriate scale factor to use: either width,
                        // height, or 1 (if the image is already smaller than 75% of viewport
                        // in both dimensions).
                        const scaleFactor = Math.min(xScale, yScale, 1);
                        const scaledWidth = naturalWidth * scaleFactor;
                        const scaledHeight = naturalHeight * scaleFactor;
                        imageCropContainer.style.width = `${scaledWidth}px`;
                        imageCropContainer.style.height = `${scaledHeight}px`;
                        // If there is already a Cropper instance, destroy it before creating a new one.
                        if (this.cropperInstance) {
                            this.cropperInstance.destroy();
                        }
                        // Create the new cropper instance, with aspectRatio set to 1 to
                        // enforce a square crop area.
                        this.cropperInstance = new Cropper(imageToCrop, {
                            aspectRatio: 1,
                            viewMode: 1,
                            autoCropArea: 1
                        });
                    }

                };
                reader.readAsDataURL(file);
            }
        },
        /**
         * Generate an image of the character based on the current appearance data.
         * @returns 
         */
        async generateCharacterImage() {
            // It shouldn't be possible to reach this function if the character is not complete,
            // but just in case, check again.
            if (!this.isComplete) {
                console.error("Character is not complete, cannot generate image.");
                showToast("Character is not complete, cannot generate image.");
                return;
            }
            // It also shouldn't be possible to reach this function if image generation is disabled, as
            // the button should not be rendered to the DOM, but check again just in case.
            if (!this.enableImageGeneration) {
                console.error("Image generation is disabled.");
                showToast("Image generation is disabled.");
                return;
            }
            // Set the isGeneratingImage flag to true so that the relevant parts of the UI
            // can be disabled.
            this.isGeneratingImage = true;

            // Create an object containing only the appearance data that is required for image generation.
            const appearanceKeys = [
                'age',                    'gender',          'height',         'build',
                'skinTone',               'hairColor',       'hairStyle',      'hairLength',
                'hairType',               'facialHairStyle', 'eyeColor',       'eyeShape',
                'distinguishingFeatures', 'clothingStyle',   'clothingColors', 'clothingAccessories'
            ];
            const appearanceData = appearanceKeys.reduce((acc, key) => {
                acc[key] = this.character[key];
                return acc;
            }, {});
            appearanceData.race = this.chosenRace.name;
            appearanceData.class = this.chosenClass.name;
            if (appearanceData.facialHairStyle !== "None" && appearanceData.facialHairStyle !== "Stubble") {
                appearanceData.facialHairLength = this.character.facialHairLength;
            }
            // Grab the CSRF token from the cookie.
            const csrfToken = getCookie('csrftoken');
            // Try to POST the appearance data to the server to generate an image.
            try {
                const response = await fetch('/characters/generate-image/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify(appearanceData)
                });
                if (!response.ok) {
                    throw new Error('Failed to POST image generation request');
                }
                const data = await response.json();
                // If successful, update the character image data with the new image url and id,
                // and set the isGeneratingImage flag to false
                this.character.image = {
                    url: data.url,
                    id: data.id
                }
                this.isGeneratingImage = false;
            } catch (error) {
                // If there is an error during the POST request, log it to the console and show a toast
                // message to the user. Also set the isGeneratingImage flag to false.
                console.error('Error POSTing image generation request:', error);
                showToast("Failed to generate image, please try again later.");
                this.isGeneratingImage = false;
            }
        }
    }));
})

