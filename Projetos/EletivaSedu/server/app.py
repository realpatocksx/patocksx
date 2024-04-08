from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath('Projetos/EletivaSedu/client'), static_folder=os.path.abspath('Projetos/EletivaSedu/client')) 

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login/index.html')

@app.route('/cadastro/')
def cadastro():
    return render_template('cadastro/index.html')

@app.route('/main/', methods=['GET', 'POST'])
def main():
    return render_template('main/index.html')

@app.route('/secao/index.html')
def secao():
    return render_template('secao/index.html')

@app.route('/painel/')
def painel():
    return render_template('painel/index.html')


if __name__ == '__main__':
    app.run(debug=True)



