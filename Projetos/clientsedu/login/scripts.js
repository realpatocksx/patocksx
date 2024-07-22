function validateForm() {
    const user = document.getElementById("user").value;
    const senha = document.getElementById("senha").value;
    const errorMessageUser = document.getElementById("error-message-user");
    const errorMessageSenha = document.getElementById("error-message-senha");

    if (user.trim() === "") {
        errorMessageUser.textContent = "Por favor, Informe seu nome de usuário.";
        return false;
    }else {
        errorMessageUser.textContent = ""; 
    }
    if (senha.trim() === "") {
        errorMessageSenha.textContent = "Por favor, Informe sua senha.";
        return false;
    } else{
        errorMessageSenha.textContent = ""; 
    }

    return true; 
}
