from flask import Flask, render_template, request, jsonify
import pandas as pd
from pytube import YouTube
import os, yt_dlp

app = Flask(__name__, template_folder=os.path.abspath('Music/client'), static_folder=os.path.abspath('Music/client'))
musicinicial = 0

# Carregar tela inicial
@app.route('/')
def index():
    tem_dados, dados = criar_excel()
    tocarmusicordem = tocarmusic()
    return render_template('index.html', tem_dados=tem_dados, dados=dados, tocarmusicordem=tocarmusicordem)

# Carregar tela playlist
@app.route('/playlist')
def playlist():
    return render_template('playlist.html')

# Gerenciar Sistema de música de add-music
@app.route('/add_music', methods=['POST'])
def add_music():
    data = request.get_json()
    music_url = data.get('music_url')
   
    caminho_arquivo = "Music/server/musics.xlsx"
    df = pd.read_excel(caminho_arquivo, engine='openpyxl')
    
    music = YouTube(music_url)
    titulo = music.title
    autor = music.author
    thumbnail = music.thumbnail_url

    add_dados = {
        "Nome Musica": titulo,
        "Nome Artista": autor,
        "URL Musica": music_url,
        "Foto Musica": thumbnail
    }

    df = pd.concat([df, pd.DataFrame([add_dados])], ignore_index=True)
    df.to_excel(caminho_arquivo, index=False, engine='openpyxl')

    return jsonify({"message": "Música adicionada com sucesso!"})

# Nova rota para processar o clique dos botões 
@app.route('/trigger_function', methods=['POST'])
def trigger_function():
    global musicinicial
    data = request.get_json()
    button_name = data.get('button')
    
    # Lógica para cada botão
    if button_name == "Play/Pause":        
        print("Função Play/Pause acionada")

        caminho_arquivo = "Music/server/musics.xlsx"
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        url = df.loc[musicinicial, 'URL Musica']
        print(url)

        # Crie o diretório se ele não existir
        download_dir = "Music/server/musics"
        os.makedirs(download_dir, exist_ok=True)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Caminho para o diretório de download
            'cookiefile': 'Music/server/cookies.txt'  # Caminho para o arquivo de cookies
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                info_dict = ydl.extract_info(url, download=False)
                title = info_dict.get('title', None)
                print(f"Download concluído: {title}.mp3")
                return jsonify({"file": os.path.join(download_dir, title + ".mp3")})
        except Exception as e:
            print(f"Erro ao baixar a música: {e}")
            return jsonify({"error": "Erro ao baixar a música"}), 500

    elif button_name == "Anterior":
        if musicinicial > 0:
            musicinicial -= 1
        caminho_arquivo = "Music/server/musics.xlsx"
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        tocarmusicordem = df.iloc[musicinicial].to_dict()  # Converte a linha para um dicionário
        return jsonify(tocarmusicordem)
    
    elif button_name == "Proximo":
        caminho_arquivo = "Music/server/musics.xlsx"
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        if musicinicial < len(df) - 1:
            musicinicial += 1
        tocarmusicordem = df.iloc[musicinicial].to_dict()  # Converte a linha para um dicionário
        return jsonify(tocarmusicordem)

    # Se o button_name não corresponder a nenhuma opção conhecida
    return jsonify({"message": f"Função para '{button_name}' não reconhecida no servidor"}), 400

def criar_excel():
    caminho_arquivo = "Music/server/musics.xlsx"
    if os.path.exists(caminho_arquivo):
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        
        # Verificando se uma coluna possui dados não nulos
        coluna1 = df['Nome Musica'].notna().any()
        coluna2 = df['Nome Artista'].notna().any()
        coluna3 = df['URL Musica'].notna().any()

        if coluna1 and coluna2 and coluna3:
            dados = df.to_dict(orient='records')
            return True, dados
        else: 
            return False, []
    else: 
        dados_music = {
            "Nome Musica": [],
            "Nome Artista": [],
            "URL Musica": [],
            "Foto Musica": []
        }

        df = pd.DataFrame(dados_music)
        df.to_excel(caminho_arquivo, index=False, engine='openpyxl')
        dados = df.to_dict(orient='records')
        return True, dados

def tocarmusic():
    caminho_arquivo = "Music/server/musics.xlsx"
    df = pd.read_excel(caminho_arquivo, engine='openpyxl')
    tocarmusicordem = df.iloc[musicinicial].to_dict()  # Converte a linha para um dicionário
    return tocarmusicordem

if __name__ == '__main__':
    app.run(debug=True)
