function verificarResposta() {
    var resposta = document.getElementById("answer").value;
    var feedbackDiv = document.getElementById("feedback");

    if (resposta == 8) {
        feedbackDiv.textContent = "Correto! Bom trabalho!";
        feedbackDiv.className = "feedback success";
    } else {
        feedbackDiv.textContent = "Incorreto! Tente novamente.";
        feedbackDiv.className = "feedback error";
    }
}
