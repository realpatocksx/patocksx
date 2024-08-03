from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__, template_folder=os.path.abspath('Music/client'), static_folder=os.path.abspath('Music/client')) 

# Carregar tela inicial
@app.route('/')
def index():
    tem_dados, dados = criar_excel()  
    return render_template('index.html', tem_dados=tem_dados, dados=dados)

# Carregar tela playlist
@app.route('/playlist')
def playlist():
    return render_template('playlist.html')

# Gerenciar Sistema de musica de add-music
@app.route('/add_music', methods=['POST'])
def add_music():
    music_url = request.form.get('music_url')
    # Aqui você pode adicionar lógica para salvar a música adicionada em um banco de dados ou arquivo
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

if __name__ == '__main__':
    app.run(debug=True)
