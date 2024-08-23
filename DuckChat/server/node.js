const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

let users = {};

io.on('connection', (socket) => {
    console.log('Novo usuário conectado.');

    socket.on('join', (username) => {
        users[socket.id] = username;
        io.emit('userJoined', `${username} entrou no chat.`);
    });

    socket.on('message', (data) => {
        io.emit('message', { user: users[socket.id], message: data.message });
    });

    socket.on('disconnect', () => {
        io.emit('userLeft', `${users[socket.id]} saiu do chat.`);
        delete users[socket.id];
    });
});

server.listen(3000, () => {
    console.log('Servidor rodando na porta 3000.');
});
