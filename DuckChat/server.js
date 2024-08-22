const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Servir arquivos estáticos, como imagens e CSS
app.use(express.static('public'));

io.on('connection', (socket) => {
    console.log('Novo usuário conectado');
    
    socket.on('sendMessage', (data) => {
        io.emit('broadcastMessage', data); // Envia a mensagem para todos os usuários
    });

    socket.on('disconnect', () => {
        console.log('Usuário desconectado');
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
