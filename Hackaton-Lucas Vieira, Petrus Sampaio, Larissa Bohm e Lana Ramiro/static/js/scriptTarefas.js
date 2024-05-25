document.addEventListener('DOMContentLoaded', () => {
    const questionElement = document.getElementById('question');
    const answerElement = document.getElementById('answer');
    const resultMessageElement = document.getElementById('result-message');
    let currentAnswer = null;

    function generateQuestion(operator) {
        let num1, num2, question, answer;

        if (operator === '+') {
            num1 = Math.floor(Math.random() * 101);
            num2 = Math.floor(Math.random() * 101);
            answer = num1 + num2;
        } else if (operator === '-') {
            num1 = Math.floor(Math.random() * 101);
            num2 = Math.floor(Math.random() * num1);
            answer = num1 - num2;
        } else if (operator === '*') {
            num1 = Math.floor(Math.random() * 11);
            num2 = Math.floor(Math.random() * 11);
            answer = num1 * num2;
        } else if (operator === '/') {
            num2 = Math.floor(Math.random() * 10) + 1;
            let result = Math.floor(Math.random() * 10) + 1;
            num1 = num2 * result;
            answer = result;
        } else {
            return;
        }

        questionElement.innerText = `Quanto é ${num1} ${operator} ${num2}?`;
        questionElement.dataset.answer = answer;
        answerElement.value = '';
        resultMessageElement.innerText = '';
        currentAnswer = answer;
    }

    window.generateQuestion = generateQuestion;

    window.checkAnswer = function() {
        const userAnswer = parseInt(answerElement.value);

        if (isNaN(userAnswer)) {
            resultMessageElement.innerText = 'Por favor, digite uma resposta válida.';
            return;
        }

        if (userAnswer === currentAnswer) {
            resultMessageElement.innerText = 'Correto! Parabéns!';
        } else {
            resultMessageElement.innerText = `Incorreto. A resposta correta é ${currentAnswer}.`;
        }
    }
});
