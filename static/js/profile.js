const editBtn = document.getElementById("edit-btn");
const editCloseBtn = document.getElementById("edit-close-btn");
const editScreen = document.getElementById("edit-screen");

editBtn.addEventListener("click", () => {
  editScreen.classList.add("show");
});

editCloseBtn.addEventListener("click", () => {
    editScreen.classList.remove("show");
});
