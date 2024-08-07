from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from pytube import YouTube
import os

app = Flask(__name__, template_folder=os.path.abspath('Music/client'), static_folder=os.path.abspath('Music/client')) 

# Carregar tela inicial
@app.route('/')
def index():
    tem_dados, dados = criar_excel()
    tocarmusicordem = tocarmusic()  # Atualizado para capturar o retorno da função tocarmusic
    return render_template('index.html', tem_dados=tem_dados, dados=dados, tocarmusicordem=tocarmusicordem)

# Carregar tela playlist
@app.route('/playlist')
def playlist():
    return render_template('playlist.html')

# Gerenciar Sistema de música de add-music
@app.route('/add_music', methods=['POST'])
def add_music():
    caminho_arquivo = "Music/server/musics.xlsx"
    df = pd.read_excel(caminho_arquivo, engine='openpyxl')
    music_url = request.form.get('music_url')
   
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

    return redirect(url_for('playlist'))

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
    musicinicial = 0
    caminho_arquivo = "Music/server/musics.xlsx"
    df = pd.read_excel(caminho_arquivo, engine='openpyxl')
    tocarmusicordem = df.iloc[musicinicial].to_dict()  # Converte a linha para um dicionário
    return tocarmusicordem

if __name__ == '__main__':
    app.run(debug=True)


'''

'''