// Função para enviar uma solicitação ao servidor Flask quando um botão é clicado
function triggerServerFunction(buttonName) {
  fetch('/trigger_function', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ button: buttonName }),
  }).then(response => response.json())
    .then(data => console.log(data.message))
    .catch((error) => console.error('Error:', error));
}

// Manipuladores de clique para os botões
document.getElementById("prev").addEventListener("click", function() {
  triggerServerFunction("Anterior");
});

document.getElementById("play-pause").addEventListener("click", function() {
  let isPlaying = this.textContent === "Pause";
  this.textContent = isPlaying ? "Play" : "Pause";
  triggerServerFunction("Play/Pause");
});

document.getElementById("next").addEventListener("click", function() {
  triggerServerFunction("Proximo");
});

// Manipulador de envio do formulário de adicionar música
document.getElementById("add-music-form").addEventListener("submit", function (event) {
  event.preventDefault(); // Impede o envio padrão do formulário

  const musicName = document.getElementById("music-name").value;
  const artistName = document.getElementById("artist-name").value;
  const musicUrl = document.getElementById("music-url").value;

  fetch('/add_music', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ music_url: musicUrl }),
  }).then(response => response.json())
    .then(data => {
        console.log(data.message);

        const playlist = document.getElementById("playlist-list");
        const li = document.createElement("li");
        li.className = "song";
        li.innerHTML = `<span>${musicName}</span> - <span>${artistName}</span> - <a href="${musicUrl}" target="_blank">Ouvir</a>`;

        playlist.appendChild(li);

        document.getElementById("add-music-form").reset();
    })
    .catch((error) => console.error('Error:', error));
});
