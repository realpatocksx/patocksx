document.addEventListener("DOMContentLoaded", function() {
    let audioElement = null;

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

                  // Se houver uma música sendo tocada, pare-a
                  if (audioElement) {
                      audioElement.pause();
                      audioElement = null;
                  }

              } else if (buttonName === "Play/Pause" && data.file) {
                  // Se um áudio estiver sendo tocado, pare-o e prepare para tocar o novo
                  if (audioElement) {
                      if (audioElement.paused) {
                          audioElement.play();
                      } else {
                          audioElement.pause();
                      }
                  } else {
                      // Crie um novo elemento de áudio para tocar a música
                      audioElement = new Audio(data.file);
                      audioElement.play().then(() => {
                          console.log(`Playing: ${data.file}`);
                      }).catch((error) => {
                          console.error('Erro ao reproduzir a música:', error);
                      });
                  }
              }
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
