from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder=os.path.abspath('Music/client'), static_folder=os.path.abspath('Music/client')) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playlist')
def playlist():
    return render_template('playlist.html')

@app.route('/add_music', methods=['POST'])
def add_music():
    music_name = request.form.get('music_name')
    artist_name = request.form.get('artist_name')
    music_url = request.form.get('music_url')
    # Aqui você pode adicionar lógica para salvar a música adicionada em um banco de dados ou arquivo
    return redirect(url_for('playlist'))

if __name__ == '__main__':
    app.run(debug=True)
