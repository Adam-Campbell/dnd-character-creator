import { 
    fetchStaticData, 
    getEmptyCharacter, 
    getCookie, 
    switchObjectNamingConventions,
    editingContexts 
} from "./utils.js";

const abilityIndexMap = {
    "strength": 0,
    "dexterity": 1,
    "constitution": 2,
    "intelligence": 3,
    "wisdom": 4,
    "charisma": 5,
    0: "strength",
    1: "dexterity",
    2: "constitution",
    3: "intelligence",
    4: "wisdom",
    5: "charisma"
}

const abilityUUIDMap = {
    "strength": "0caab33e-f424-4a44-94cd-0c6951e5bdfe",
    "dexterity": "fd107c7f-4536-4b36-bf43-e49d92a3c4c2",
    "constitution": "b9b14f85-78db-49ea-b07b-b8bdd7a40046",
    "intelligence": "44fbcb3c-d548-4a3c-aa85-4c55e05aabed",
    "wisdom": "468b3218-340b-4263-9450-dc72e6750f16",
    "charisma": "b15c2aa9-87e7-408d-89a7-3bbd64d981a9"
}




document.addEventListener("alpine:init", () => {
    console.log("alpine has initialised");
    Alpine.prefix("data-")
    Alpine.data('characterGenerator', () => ({
        character: null,
        staticData: null,
        isLoading: true,
        currentPage: "race",
        editingContext: null,
        characterId: null,

        async init() {
            console.log("cg init ran")
            try {
                console.log("cg init ran")
                this.isLoading = true;
                this.staticData = await fetchStaticData();
                //console.log(this.staticData)
                this.setInitialState();
                this.isLoading = false;
            } catch (error) {
                console.error('Error fetching JSON:', error);
            }
        },
        setInitialState() {
            if (window.editorData) {
                const { editingContext, characterData, characterId } = window.editorData;
                this.editingContext = editingContext;
                this.characterId = characterId;
                if (editingContext === editingContexts.editExisting || editingContext === editingContexts.cloneExisting) {
                    this.character = switchObjectNamingConventions(characterData);
                } else {
                    this.character = getEmptyCharacter();
                }
            }
        },
        setPage(page) {
            this.currentPage = page;
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
        get isCaster() {
            return this.chosenClass.spellcasting.ability !== null;
        },
        get isComplete() {
            // Race page doesn't need to be checked
            // Check class page
            if (this.character.classSkillChoices.length !== this.computedNumberOfSkillProficiencies) {
                return false;
            }
            // Check ability point page
            for (let i = 0; i < this.character.abilityPoints.length; i++) {
                if (this.character.abilityPoints[i].value === "--") {
                    return false;
                }
            }
            // Check cantrips and spells page
            if (this.isCaster) {
                if (this.character.classCantripChoices.length !== this.chosenClass.spellcasting.cantrips.choose) {
                    return false;
                }
                if (this.character.classSpellChoices.length !== this.chosenClass.spellcasting.spells.choose) {
                    return false;
                }
            }
            // Check background page
            if (this.character.name === "" || this.character.age === "" || this.character.gender === "" || this.character.background === "") {
                return false;
            }
            // Check appearance page
            if (this.character.height === "" || this.character.build === "" || this.character.skinTone === "" || this.character.eyeColor === "" || 
                this.character.hairColor === "" || this.character.hairStyle === "" || this.character.clothingStyle === "" || this.character.clothingColors === "") {
                return false;
            }
            return true;
        },
        /**
         * Get the current base score for the given ability, with no bonuses applied.
         * @param {*} abilityName 
         * @returns 
         */
        getAbilityBaseScore(abilityUUID) {
            //const idx = abilityIndexMap[abilityName];
            const ability = this.character.abilityPoints.find(a => a.id === abilityUUID);
            return ability.value;
            //return this.character.abilityPoints[idx].value;
        },
        /**
         * Get the racial ability bonus for the given ability.
         * @param {*} abilityName 
         * @returns 
         */
        getRacialAbilityBonus(abilityUUID) {
            //const idx = abilityIndexMap[abilityName];
            const bonus = this.chosenRace.abilityBonuses.find(a => a.ability.id === abilityUUID);
            return bonus.bonus;
            //const bonus = this.chosenRace.abilityBonuses[idx];;
            //return bonus.bonus;
        },
        /**
         * Get the ability score for the given ability, with racial bonuses applied.
         * @param {*} abilityName 
         * @returns 
         */
        getAdjustedAbilityScore(abilityUUID) {
            //const idx = abilityIndexMap[abilityName];
            //const baseScore = this.character.abilityPoints[idx].value;
            //const racialBonus = this.getRacialAbilityBonus(abilityName);
            const baseScore = this.getAbilityBaseScore(abilityUUID);
            const racialBonus = this.getRacialAbilityBonus(abilityUUID);
            if (baseScore === "--") {
                return "--";
            } else {
                return baseScore + racialBonus;
            }
        },
        /**
         * Get the modifier for the given ability (adjusted).
         * @param {*} abilityName 
         * @returns 
         */
        getAbilityModifier(abilityUUID) {
            const score = this.getAdjustedAbilityScore(abilityUUID);
            if (score === "--") {
                return 0;
            }
            return Math.floor((score - 10) / 2);
        },
        /**
         * Adds or removes the given skillId from the classSkillChoices array. Respects the
         * computedNumberOfSkillProficiencies, removing the oldest skill if the user tries to
         * add more than the allowed number.
         * @param {*} skillId 
         */
        toggleSkillProficiency(skillId) {
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
         * @param {*} abilityId 
         * @returns 
         */
        getAbilityData(abilityId) {
            return this.staticData.abilities.find(a => a.id === abilityId);
        },
        /**
         * Computes the ability point options for the given abilityId, based on which
         * points from the standard array have already been chosen.
         * @param {*} abilityId 
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
            if (points[0] !== "--") {
                points.unshift("--");
            }
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
         * Any cleanup that needs to happen when the race is changed goes here.
         * (example: resetting class skill proficiency choices, as the race choice
         * can affect how many skills the class can choose).
         */
        resetStateOnRaceChange() {
            this.character.classSkillChoices = [];
        },
        /**
         * Whenever a different class is chosen, reset the relevant parts of state, either
         * to empty or to the class default.
         * @param {*} e 
         */
        resetStateOnClassChange(e) {
            this.character.classSkillChoices = [];
            this.character.classCantripChoices = [];
            this.character.classSpellChoices = [];
        },
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
        removeCantrip(cantripId) {
            // If the cantrip is not in the list, do nothing.
            if (!this.character.classCantripChoices.includes(cantripId)) {
                console.error("Attempted to remove a cantrip that is not in the list.");
                return;
            }
            this.character.classCantripChoices = this.character.classCantripChoices.filter(c => c !== cantripId);
        },
        getCantripData(cantripId) {
            return this.staticData.spells.find(c => c.id === cantripId);
        },
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
        removeSpell(spellId) {
            // If the spell is not in the list, do nothing.
            if (!this.character.classSpellChoices.includes(spellId)) {
                console.error("Attempted to remove a cantrip that is not in the list.");
                return;
            }
            this.character.classSpellChoices = this.character.classSpellChoices.filter(s => s !== spellId);
        },
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
            // If the new style is None or Stubble, then the length should be None.
            if (newStyle === "None" || newStyle === "Stubble") {
                this.character.facialHairLength = "";
            // If the new style is not None or Stubble, and the length is None, then set it to Short,
            // but don't overwrite if it is already set to something else.
            } else if (this.character.facialHairLength === "") {
                this.character.facialHairLength = "Short";
            }
        },
        /**
         * Truncates the given text if it is longer than maxLength, adding '...' to the end.
         * @param {*} text 
         * @param {*} maxLength 
         * @returns 
         */
        truncateText(text, maxLength) {
            // This implementation will suffice for now. However, we should ensure that
            // it doesn't cut off mid-word or mid line-break (\n). Either truncate more
            // or less if this happens. 
            if (text.length > maxLength) {
                return text.slice(0, maxLength) + '...';
            }
            return text;
        },
        /**
         * Replaces line breaks in the given text with <br> tags, which will be respected by HTML.
         * @param {*} text 
         * @returns 
         */
        formatLineBreaks(text) {
            return text.replace(/(?:\r\n|\r|\n)/g, '<br/>');
        },
        /**
         * When the user has finished creating their character, POST the character to the server.
         */
        async handleSubmit(e) {
            console.log("handleSubmit called")
            e.preventDefault();
            console.log(this.character);
            const csrfToken = getCookie('csrftoken');
            const python_ready_character = switchObjectNamingConventions(this.character);
            console.log(python_ready_character)
            let url = '';
            if (this.editingContext === editingContexts.editExisting) {
                url = `/characters/${this.characterId}/edit/`;
            } else {
                url = '/characters/new/';
            }
            try {
                // let url = '/characters/new/';
                // if (python_ready_character.id) {
                //     url = `/characters/${python_ready_character.id}/edit/`;
                // }
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
                console.log('Success', data);
            } catch (error) {
                console.error('Error POSTing character:', error);
            }
        }
    }));
})

