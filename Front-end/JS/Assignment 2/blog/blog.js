document.addEventListener("DOMContentLoaded", function () {
    const showAnswerButtons = document.querySelectorAll(".show-answer");
    showAnswerButtons.forEach(button => {
        button.addEventListener("click", function () {
            const answer = this.nextElementSibling;
            answer.style.display = answer.style.display === "block" ? "none" : "block";
        });
    });
});