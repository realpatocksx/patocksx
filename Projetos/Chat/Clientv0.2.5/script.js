function filterUsers() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const users = document.querySelectorAll(".user");
    
    users.forEach(user => {
        const username = user.textContent.toLowerCase();
        user.style.display = username.includes(input) ? "" : "none";
    });
}

function selectContact(contact) {
    // Atualizar informações de contato
}

function deleteMessage(messageElement) {
    if (confirm("Deseja excluir esta mensagem?")) {
        messageElement.remove();
    }
}

// Envio de mensagem
document.querySelector(".message-input button").onclick = function() {
    const input = document.querySelector(".message-input input[type='text']");
    const messageText = input.value;
    if (messageText) {
        const messageDiv = document.createElement("div");
        messageDiv.className = "message sent";
        messageDiv.innerHTML = `<span>Eu: ${messageText}</span>`;
        document.getElementById("chatWindow").appendChild(messageDiv);
        input.value = ''; // Limpar campo de entrada
    }
};

function openSettings() {
    alert("Abrindo configurações...");
    // Aqui você pode implementar a lógica para abrir as configurações
}
