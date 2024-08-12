import yt_dlp
import pygame
import os

def download_music(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'cookiefile': 'Music/server/cookies.txt'  # Caminho para o arquivo de cookies
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        title = info_dict.get('title', None)
        print(f"Download concluído: {title}.mp3")
        return title + ".mp3"

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print("Tocando música...")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

youtube_url = "https://www.youtube.com/watch?v=SEomzWa9PHU"
music_file = download_music(youtube_url)
play_music(music_file)
