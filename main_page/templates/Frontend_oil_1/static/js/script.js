// function changeContent(element) {
//     element.innerHTML += <i class="fa-solid fa-arrow-right"></i>;
// }

document.getElementById("show_form_button").addEventListener("click", function() {
    document.getElementById("overlay").style.display = "grid";
    document.getElementById("request_form_overlay").style.display = "block";
    document.getElementById("feedback-box").style.width = '520px';
    document.getElementById("overlay-title").style.fontSize = '14px';
    document.getElementById("feedback-box").style.gridTemplateColumns = '1fr';
});

document.getElementById("overlay").addEventListener("click", function() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("request_form_overlay").style.display = "none";
});