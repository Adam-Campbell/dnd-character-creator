import { getCookie } from './utils.js';
import { showToast } from './toast.js';


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
                showToast('Character deleted successfully!', { variant: 'success', delay: 2000, callback: () => window.location.href = '/characters/' });
                //window.location.href = '/characters/';
            }
        } catch (error) {
            console.error('Error deleting character:', error);
            showToast('Failed to delete character. Please try again later.');
        }
    });
}

