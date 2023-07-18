

function openFunction() {
    document.getElementById('addtask').style.display = "flex";
}

function closeFunction() {
    document.getElementById('addtask').style.display = "none";
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('plus_id').addEventListener("click", openFunction);
    document.getElementById('close_button').addEventListener("click", closeFunction);
})

