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

