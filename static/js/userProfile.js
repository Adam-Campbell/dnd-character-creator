import { getCookie } from './utils.js';

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
const cropImageButton = document.getElementById("crop-image-button");
const cropCancelButton = document.getElementById("crop-cancel-button");
const imageModalOverlay = document.getElementById('image-modal-overlay');
const imageCropContainer = document.getElementById('image-crop-container');
let cropperInstance = null;

imageCropContainer.innerHTML = `<img id="image-to-crop" src="" alt="Cropped image">`;

if (imageInput) {
    imageInput.addEventListener("change", (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                
    
                imageModalOverlay.style.display = 'flex';
                
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

cropImageButton.addEventListener('click', () => {
    if (cropperInstance) {
        const data = cropperInstance.getData();
        const croppedWidth = Math.min(data.width, 500);
        cropperInstance.getCroppedCanvas({ width: croppedWidth }).toBlob(async (blob) => {
            const formData = new FormData();
            formData.append('image', blob);
            const csrfToken = getCookie('csrftoken');
            const userId = imageInput.dataset.userId;
            const url = `/profile/${userId}/upload-image/`;
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
                location.reload();
                
                imageModalOverlay.style.display = 'none';
                
            } catch (error) {
                console.error('Error POSTing image:', error);
            }
        })
    }
});

cropCancelButton.addEventListener('click', () => {
    if (cropperInstance) {
        cropperInstance.destroy();
    }
    imageModalOverlay.style.display = 'none';
});