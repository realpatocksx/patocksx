from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath('Projetos/EletivaSedu/client'), static_folder=os.path.abspath('Projetos/EletivaSedu/client')) 

titulo = 'Teste da Sucao da segundo quinta'
titulo2 = 'Vai Toma no Seu'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html', Titulo=titulo, Titulo2=titulo2)

@app.route('/secao/index.html')
def secao():
    return render_template('secao/index.html', Titulo=titulo, Titulo2=titulo2)

@app.route('/painel/')
def painel():
    return render_template('painel/index.html')

@app.route('/login/')
def login():
    return render_template('login/index.html')

@app.route('/cadastro/')
def cadastro():
    return render_template('cadastro/index.html')

if __name__ == '__main__':
    app.run(debug=True)
