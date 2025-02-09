console.log("hello from userProfile.js");

const bioContainer = document.getElementById("bio-container");
const editBioButton = document.getElementById("edit-bio-button");
const editBioForm = document.getElementById("edit-bio-form");

if (editBioButton) {
    editBioButton.addEventListener("click", () => {
        bioContainer.classList.add("d-none");
        editBioForm.classList.remove("d-none")
    });
}

const imageInput = document.getElementById("image-upload");
let cropperInstance = null;


if (imageInput) {
    imageInput.addEventListener("change", (e) => {
        console.log("image input change event");
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const imageModalOverlay = document.getElementById('image-modal-overlay');
    
                imageModalOverlay.style.display = 'flex';
                const imageCropContainer = document.getElementById('image-crop-container');
                const imageToCrop = document.getElementById('image-to-crop');
                imageToCrop.src = e.target.result;
                imageToCrop.onload = () => {

                    const naturalWidth = imageToCrop.naturalWidth;
                    const naturalHeight = imageToCrop.naturalHeight;
                    const viewportWidth = window.innerWidth;
                    const viewportHeight = window.innerHeight;

                    const xScale = (viewportWidth * 0.75) / naturalWidth;
                    const yScale = (viewportHeight * 0.75) / naturalHeight;

                    const scaleFactor = Math.min(xScale, yScale);
                    const scaledWidth = naturalWidth * scaleFactor;
                    const scaledHeight = naturalHeight * scaleFactor;
                    imageCropContainer.style.width = `${scaledWidth}px`;
                    imageCropContainer.style.height = `${scaledHeight}px`;

                    if (cropperInstance) {
                        cropperInstance.destroy();
                    }
                    cropperInstance = new Cropper(imageToCrop, {
                        aspectRatio: 1,
                        viewMode: 1,
                        autoCropArea: 1
                    });
                }

            };
            reader.readAsDataURL(file);
        }
    });
}