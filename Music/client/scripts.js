document.addEventListener("DOMContentLoaded", function() {
  function triggerServerFunction(buttonName) {
    fetch('/trigger_function', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ button: buttonName }),
    }).then(response => response.json())
      .then(data => {
          if (buttonName === "Proximo" || buttonName === "Anterior") {
              // Atualize os elementos com os dados da música
              document.getElementById("music-title").textContent = data['Nome Musica'];
              document.getElementById("music-artist").textContent = data['Nome Artista'];
              document.getElementById("music-thumbnail").src = data['Foto Musica'];
          }
          console.log(data.message);
      })
      .catch((error) => console.error('Error:', error));
  }

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
});
