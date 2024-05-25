document.addEventListener('DOMContentLoaded', () => {
    const loginMessageElement = document.getElementById('login-message');

    window.login = function() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const storedUser = localStorage.getItem(username);
        open('/tarefas')
        if (storedUser) {
            const user = JSON.parse(storedUser);
            if (user.password === password) {
                loginMessageElement.innerText = 'Login bem-sucedido!';
                localStorage.setItem('currentUser', username);
                window.location.href = 'tarefas.html';
            } else {
                loginMessageElement.innerText = 'Senha incorreta. Tente novamente.';
            }
        } else {
            loginMessageElement.innerText = 'Usuário não encontrado. Tente novamente.';
        }
    };
});

login = function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const storedUser = localStorage.getItem(username);
    open('tarefas.html')
    if (storedUser) {
        const user = JSON.parse(storedUser);
        if (user.password === password) {
            loginMessageElement.innerText = 'Login bem-sucedido!';
            localStorage.setItem('currentUser', username);
            window.location.href = 'tarefas.html';
        } else {
            loginMessageElement.innerText = 'Senha incorreta. Tente novamente.';
        }
    } else {
        loginMessageElement.innerText = 'Usuário não encontrado. Tente novamente.';
    }
};
