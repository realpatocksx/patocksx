from flask import Flask, render_template, redirect, url_for, request
import mysql.connector
import os 

app = Flask(__name__, template_folder=os.path.abspath('teste/client'))

db = mysql.connector.connect(
    host="51.81.166.66",
    user="u2243734_R5q046VDMu",
    password="Qqz3DIISHcvYQSPZMD^gx!bI",
    database="s2243734_cadastro"
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM noticias")
    noticias = cursor.fetchall()
    if not noticias:
        return redirect(url_for('cadastro'))
    return render_template('index.html', noticias=noticias)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        foto = request.form['foto']
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        cursor.execute("INSERT INTO noticias (foto, titulo, descricao) VALUES (%s, %s, %s)", (foto, titulo, descricao))
        db.commit()
        return redirect(url_for('index'))
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)

