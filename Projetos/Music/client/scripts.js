document.getElementById("play-pause").addEventListener("click", function () {
  let isPlaying = this.textContent === "Pause";
  this.textContent = isPlaying ? "Play" : "Pause";
});

document
  .getElementById("add-music-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const musicName = document.getElementById("music-name").value;
    const artistName = document.getElementById("artist-name").value;
    const musicUrl = document.getElementById("music-url").value;

    const playlist = document.getElementById("playlist-list");
    const li = document.createElement("li");
    li.className = "song";
    li.innerHTML = `<span>${musicName}</span> - <span>${artistName}</span> - <a href="${musicUrl}" target="_blank">Ouvir</a>`;

    playlist.appendChild(li);

    document.getElementById("add-music-form").reset();
  });
