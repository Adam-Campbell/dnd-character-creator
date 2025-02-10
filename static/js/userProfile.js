import { getCookie } from './utils.js';
import { showToast } from './toast.js';


const bioContainer = document.getElementById("bio-container");
const editBioButton = document.getElementById("edit-bio-button");
const editBioForm = document.getElementById("edit-bio-form");

if (editBioButton) {
    editBioButton.addEventListener("click", () => {
        bioContainer.classList.add("d-none");
        editBioForm.classList.remove("d-none");
    });
}

const imageInput = document.getElementById("image-upload");
const cropImageButton = document.getElementById("crop-image-button");
const cropCancelButton = document.getElementById("crop-cancel-button");
const imageModalOverlay = document.getElementById('image-modal-overlay');
const imageCropContainer = document.getElementById('image-crop-container');
let cropperInstance = null;

if (imageInput) {
    imageInput.addEventListener("change", (e) => {
        // Get the file that the user selected.
        const file = e.target.files[0];
        if (file) {
            // Create a FileReader to read the file as a data URL.
            // When the file is loaded, display the image and create
            // a Cropper instance.
            const reader = new FileReader();
            reader.onload = (e) => {
                imageModalOverlay.style.display = 'flex';
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
                    if (cropperInstance) {
                        cropperInstance.destroy();
                    }
                    // Create the new cropper instance, with aspectRatio set to 1 to
                    // enforce a square crop area.
                    cropperInstance = new Cropper(imageToCrop, {
                        aspectRatio: 1,
                        viewMode: 1,
                        autoCropArea: 1
                    });
                };

            };
            reader.readAsDataURL(file);
        }
    });
}

// Add event listener to the crop image button
cropImageButton.addEventListener('click', () => {
    if (cropperInstance) {
        const data = cropperInstance.getData();
        const croppedWidth = Math.min(data.width, 500);
        // On click, retrieve cropped image from cropper instance, convert to blob, and POST to server.
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
                imageModalOverlay.style.display = 'none';
                showToast('Image uploaded successfully!', { variant: 'success', delay: 2000, callback: () => window.location.reload() });
                
            } catch (error) {
                console.error('Error POSTing image:', error);
                showToast('Failed to upload image. Please try again later.');
            }
        });
    }
});

// Add event listener to the cancel crop button
cropCancelButton.addEventListener('click', () => {
    // Destroy the Cropper instance and hide the modal overlay
    if (cropperInstance) {
        cropperInstance.destroy();
    }
    imageModalOverlay.style.display = 'none';
});