from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = 'admin2025'
global user
caminho_excel_registros = 'Chat/static/data/registros.xlsx'
caminho_excel_mensagens = 'Chat/static/data/mensagens.xlsx'


@app.route('/')
def inicio():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    excel()  # Certifique-se de que os arquivos Excel existem
    load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")
    global user

    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        verificar_user = user in load_excel['User'].values
        linha = load_excel[load_excel['User'] == user]

        if verificar_user:
            linha_password = str(linha.iloc[0]['Password'])
            if password == linha_password:
                # Carrega as mensagens ao acessar o chat
                return redirect(url_for('chat'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    excel()
    add_registro = {}
    load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")

    if request.method == 'POST':
        user = request.form.get('username').strip()
        for letra in user:
            if letra in [' ', '.', ',', '@', '#', '*', '/', '\,', '|', '?', '$', '', '%']:
                return render_template('register.html')        
        if not user: 
            return render_template('register.html')
        elif len(user) < 5: 
            return render_template('register.html')
        elif len(user) > 12:
            return render_template('register.html')
        else: 
            user = user

        gmail = request.form.get('email').strip()
       
        password = request.form.get('password').strip()
        if not password:
            return render_template('register.html')
        elif len(password) < 5:
            return render_template('register.html')
        elif len(password) > 12:
            return render_template('register.html')
        elif password == user:
            return render_template('register.html')
        else: 
            password = password

        passwordconfim = request.form.get('passwordconfirm')
        if not password == passwordconfim:
             return render_template('register.html')
        
        add_registro = {
            'User': user,
            'Password': password
        }

        load_excel = pd.concat([load_excel, pd.DataFrame([add_registro])], ignore_index=True)
        load_excel.to_excel(caminho_excel_registros, index=False, engine='openpyxl')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/chat')
def chat():
    # Carrega as mensagens do Excel para exibir na página de chat
    load_excel_mensagens = pd.read_excel(caminho_excel_mensagens, engine='openpyxl')
    dados = load_excel_mensagens.to_dict(orient='records')

    # Renderiza a página de chat com as mensagens carregadas
    return render_template('chat.html', dados=dados)


def excel():
    if os.path.exists(caminho_excel_registros): 
        load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")

    else:
        criar_excel_registros = {
            "User": [],
            "Gmail": [],
            "Password": []
        }

        load_excel = pd.DataFrame(criar_excel_registros)
        load_excel.to_excel(caminho_excel_registros, index=False , engine='openpyxl')
    
    if os.path.exists(caminho_excel_mensagens):
        load_excel_mensagens = pd.read_excel(caminho_excel_mensagens, engine='openpyxl')

    else:
        criar_excel_mensagens = {
            "User": [],
            "Mensagem": [],
            "Hora": [],
            "ID": []
        }

        load_excel_mensagens = pd.DataFrame(criar_excel_mensagens)
        load_excel_mensagens.to_excel(caminho_excel_mensagens, index=False, engine='openpyxl')

@app.route('/enviar_messagem', methods=["POST"])
def enviar_messagem():
    load_excel_mensagens = pd.read_excel(caminho_excel_mensagens, engine='openpyxl')
    mensagem = request.form.get('message')
    hora = 'Ainda criando'
    ID = 'Ainda criando'

    add_mensagens = {
        "User": user,
        "Mensagem": mensagem,
        "Hora": hora,
        "ID": ID
    }

    load_excel_mensagens = pd.concat([load_excel_mensagens, pd.DataFrame([add_mensagens])], ignore_index=True)
    load_excel_mensagens.to_excel(caminho_excel_mensagens, index=False, engine='openpyxl')

    # Recarrega as mensagens após enviar a nova mensagem
    dados = load_excel_mensagens.to_dict(orient='records')
    return render_template('chat.html', dados=dados)


if __name__ == '__main__':
    app.run(debug=True)