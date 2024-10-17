from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
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
    print(f"Acessando arquivo: {caminho_arquivo}")

    try:
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return jsonify({"error": "Erro ao ler o arquivo."}), 500

    titulo, autor, thumbnail = get_video_info(music_url)

    if not titulo or not autor:
        return jsonify({"error": "Erro ao obter informações do vídeo."}), 500

    add_dados = {
        "Nome Musica": titulo,
        "Nome Artista": autor,
        "URL Musica": music_url,
        "Foto Musica": thumbnail
    }

    df = pd.concat([df, pd.DataFrame([add_dados])], ignore_index=True)
    
    try:
        df.to_excel(caminho_arquivo, index=False, engine='openpyxl')
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
        return jsonify({"error": "Erro ao salvar o arquivo."}), 500

    return jsonify({"message": "Música adicionada com sucesso!"})

# Função para capturar informações do vídeo usando yt-dlp
def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', 'Título Desconhecido')
            author = info_dict.get('uploader', 'Autor Desconhecido')
            thumbnail = info_dict.get('thumbnail', None)
            return title, author, thumbnail
        except Exception as e:
            print(f"Erro ao extrair informações do vídeo: {e}")
            return None, None, None

# Nova rota para processar o clique dos botões 
@app.route('/trigger_function', methods=['POST'])
def trigger_function():
    global musicinicial
    data = request.get_json()
    button_name = data.get('button')
    
    if button_name == "Play/Pause":        
        print("Função Play/Pause acionada")

        caminho_arquivo = "Music/server/musics.xlsx"
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        url = df.loc[musicinicial, 'URL Musica']
        title = df.loc[musicinicial, 'Nome Musica']
        download_dir = os.path.join(os.getcwd(), "Music/server/musics")
        file_path = os.path.join(download_dir, f"{title}.mp3")

        # Verificar se o arquivo já existe
        if not os.path.exists(file_path):
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(download_dir, f"{title}.%(ext)s"),  # Remove a extensão .mp3 do outtmpl
                'cookiefile': 'Music/server/cookies.txt'
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                    print(f"Download concluído: {title}.mp3")
            except Exception as e:
                print(f"Erro ao baixar a música: {e}")
                return jsonify({"error": "Erro ao baixar a música"}), 500

        # Retornar o caminho da música
        return jsonify({"file": f"/play_music/{musicinicial}"})
    
    elif button_name == "Anterior":
        if musicinicial > 0:
            musicinicial -= 1
        caminho_arquivo = "Music/server/musics.xlsx"
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        tocarmusicordem = df.iloc[musicinicial].to_dict()  
        return jsonify(tocarmusicordem)
    
    elif button_name == "Proximo":
        caminho_arquivo = "Music/server/musics.xlsx"
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        if musicinicial < len(df) - 1:
            musicinicial += 1
        tocarmusicordem = df.iloc[musicinicial].to_dict()  
        return jsonify(tocarmusicordem)

    return jsonify({"message": f"Função para '{button_name}' não reconhecida no servidor"}), 400


# Nova rota para servir a música protegida
@app.route('/play_music/<int:music_index>', methods=['GET'])
def play_music(music_index):
    caminho_arquivo = "Music/server/musics.xlsx"
    df = pd.read_excel(caminho_arquivo, engine='openpyxl')
    title = df.loc[music_index, 'Nome Musica']
    
    # Aqui, assegure que o caminho seja correto e não tenha duplicação
    download_dir = os.path.join(os.getcwd(), "Music/server/musics")  # Garante que o caminho seja relativo à raiz do projeto
    file_path = os.path.join(download_dir, f"{title}.mp3")
    
    if not os.path.exists(file_path):
        return jsonify({"error": "Arquivo não encontrado."}), 404
    
    return send_file(file_path, as_attachment=False, download_name=f"{title}.mp3")

def criar_excel():
    caminho_arquivo = "Music/server/musics.xlsx"
    if os.path.exists(caminho_arquivo):
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        
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
    tocarmusicordem = df.iloc[musicinicial].to_dict()  
    return tocarmusicordem

if __name__ == '__main__':
    app.run(debug=True)


'''
@app.route('/add_music', methods=['POST'])
def add_music():
    data = request.get_json()
    music_url = data.get('music_url')

    caminho_arquivo = "Music/server/musics.xlsx"
    print(f"Acessando arquivo: {caminho_arquivo}")

    try:
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return jsonify({"error": "Erro ao ler o arquivo."}), 500

    titulo, autor, thumbnail = get_video_info(music_url)

    if not titulo or not autor:
        return jsonify({"error": "Erro ao obter informações do vídeo."}), 500

    add_dados = {
        "Nome Musica": titulo,
        "Nome Artista": autor,
        "URL Musica": music_url,
        "Foto Musica": thumbnail
    }

    df = pd.concat([df, pd.DataFrame([add_dados])], ignore_index=True)
    
    try:
        df.to_excel(caminho_arquivo, index=False, engine='openpyxl')
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
        return jsonify({"error": "Erro ao salvar o arquivo."}), 500

    return jsonify({"message": "Música adicionada com sucesso!"})

https://youtu.be/SEomzWa9PHU?si=HC7tiEb0vNk994Qj

'''