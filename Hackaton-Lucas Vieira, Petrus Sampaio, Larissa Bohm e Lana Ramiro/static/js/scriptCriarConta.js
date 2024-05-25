document.addEventListener('DOMContentLoaded', () => {
    const registerMessageElement = document.getElementById('register-message');

    // Função para processar a criação de conta
    window.criarConta = function() {
        const newUsername = document.getElementById('new-username').value;
        const newPassword = document.getElementById('new-password').value;
        open('/index.html')

        if (localStorage.getItem(newUsername)) {
            registerMessageElement.innerText = 'Usuário já existe. Escolha um nome de usuário diferente.';
        } else {
            const newUser = {
                username: newUsername,
                password: newPassword,
                balance: 100 // Inicialize o saldo do usuário com 100 tucoins
            };
            localStorage.setItem(newUsername, JSON.stringify(newUser));
            registerMessageElement.innerText = 'Conta criada com sucesso! Redirecionando para o login...';
            setTimeout(() => {
                window.location.href = 'index.html';
            }, 2000); // Redireciona após 2 segundos
        }
    };
});

criarConta = function() {
    const newUsername = document.getElementById('new-username').value;
    const newPassword = document.getElementById('new-password').value;
    open('index.html')

    if (localStorage.getItem(newUsername)) {
        registerMessageElement.innerText = 'Usuário já existe. Escolha um nome de usuário diferente.';
    } else {
        const newUser = {
            username: newUsername,
            password: newPassword,
            balance: 100 // Inicialize o saldo do usuário com 100 tucoins
        };
        localStorage.setItem(newUsername, JSON.stringify(newUser));
        registerMessageElement.innerText = 'Conta criada com sucesso! Redirecionando para o login...';
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 2000); // Redireciona após 2 segundos
    }
};