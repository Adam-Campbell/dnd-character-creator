import { getCookie } from './utils.js';
console.log("Hello from characterDetail.js");

const confirmDeleteButton = document.getElementById('confirm-delete-button');


if (confirmDeleteButton) {
    confirmDeleteButton.addEventListener('click', async () => {
        const characterId = confirmDeleteButton.getAttribute('data-character-id');
        try {
            const response = await fetch(`/characters/${characterId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            if (response.ok) {
                const deletionConfirmationModal = document.getElementById('deletionConfirmationModal');
                const modal = bootstrap.Modal.getInstance(deletionConfirmationModal);
                modal.hide();
                window.location.href = '/characters/';
            }
        } catch (error) {
            console.error('Error deleting character:', error);
        }
    });
}

