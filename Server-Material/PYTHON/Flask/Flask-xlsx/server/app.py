from flask import Flask, render_template, request, redirect
from openpyxl import Workbook, load_workbook
import pandas as pd
import os


app = Flask(__name__, template_folder=os.path.abspath('Server-Material/PYTHON/Flask/Flask-xlsx/client'))

# Lista para armazenar os dados das inscrições
inscricoes = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inscricao', methods=['POST'])
def inscrever():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    inscricao = {'nome': nome, 'email': email, 'telefone': telefone}
    inscricoes.append(inscricao) 

    # Salvar os dados em um arquivo Excel
    df = pd.DataFrame(inscricoes)
    df.to_excel('Server-Material/PYTHON/Flask/Flask-xlsx/server/inscricoes.xlsx', index=False)

    return redirect('/')

@app.route('/dados')
def listar_dados():
    df = pd.read_excel('Server-Material/PYTHON/Flask/Flask-xlsx/server/inscricoes.xlsx')
    inscricoes = df.to_dict('records')
    return render_template('dados.html', inscricoes=inscricoes)

@app.route('/dados/<int:index>')
def detalhar_dado(index):
    inscricao = inscricoes[index]
    return render_template('detalhe.html', inscricao=inscricao)

@app.route('/login')
def login():
    df = pd.read_excel('Server-Material/PYTHON/Flask/Flask-xlsx/server/inscricoes.xlsx')

    # Obtém o valor da terceira célula da coluna A
    valor_A3 = df.iloc[2, 0]
    return render_template('login.html', valor_A3=valor_A3)

if __name__ == '__main__':
    app.run(debug=True)