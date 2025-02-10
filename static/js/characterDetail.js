import { getCookie } from './utils.js';
import { showToast } from './toast.js';


const confirmDeleteButton = document.getElementById('confirm-delete-button');


if (confirmDeleteButton) {
    // Add event listener that sends a DELETE request to the server
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
                // If deletion was successful, hide the modal, show a success toast to the user
                // and redirect to the characters list page after a delay
                const deletionConfirmationModal = document.getElementById('deletionConfirmationModal');
                const modal = bootstrap.Modal.getInstance(deletionConfirmationModal);
                modal.hide();
                showToast('Character deleted successfully!', { variant: 'success', delay: 2000, callback: () => window.location.href = '/characters/' });
            }
        } catch (error) {
            // If an error occurs, log it to the console and show an error toast to the user
            console.error('Error deleting character:', error);
            showToast('Failed to delete character. Please try again later.');
        }
    });
}

