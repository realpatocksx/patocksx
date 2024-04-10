function validateForm() {
    const user = document.getElementById("user").value;
    const senha = document.getElementById("senha").value;
    const namecomplet = document.getElementById("namecomplet").value;
    const errorMessageName = document.getElementById("error-message-name");
    const errorMessageUser = document.getElementById("error-message-user");
    const errorMessageSenha = document.getElementById("error-message-senha");

    if (namecomplet.trim() === "") {
        errorMessageName.textContent = "Por favor, preencha o seu nome completo.";
        return false;
    }else {
        errorMessageName.textContent = ""; 
    }
    if (user.trim() === "") {
        errorMessageUser.textContent = "Por favor, crie seu nome de usuário.";
        return false;
    }else {
        errorMessageUser.textContent = ""; 
    }
    if (senha.trim() === "") {
        errorMessageSenha.textContent = "Por favor, crie sua senha.";
        return false;
    } else{
        errorMessageSenha.textContent = ""; 
    }

    return true; 
}

document.getElementById('cargo').onchange = function() {
    const cargo = this.value;
    const divTurma = document.getElementById('divTurma');
    const email = document.getElementById('email').value
    const errorMessageemail = document.getElementById("error-message-email");
    if (cargo === 'Aluno') {
        divTurma.style.display = 'block';
    } else {
        divTurma.style.display = 'none';
        if (email.trim() === "") {
            errorMessageemail.textContent = 'Por favor, Informe o seu email';
        }else{
            errorMessageemail.textContent = '';
        }
    }
};
