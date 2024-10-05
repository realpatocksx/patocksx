from flask import Flask, render_template, request, redirect, url_for, flash
import os, random
import pandas as pd

app = Flask(__name__)
app.secret_key = 'admin1230270225'

global user #da uma olhada 

global gamil #ve o codigo pois acho que nao preciso mmas 
global password# ve o codigo pois acho que nao preciso mmas 


caminho_excel_registros = 'Chat/static/data/registros.xlsx'
caminho_excel_mensagens = 'Chat/static/data/mensagens.xlsx'


@app.route('/')
def inicio():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    excel()  
    load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")
    global user

    if request.method == 'POST':
        user = request.form.get('username').strip()
        if not user:
            flash('O Nome de Usuario nao pode ficar vazio!', 'user')
            return render_template('login.html')
        password = request.form.get('password')
        if not password:
            flash('A Senha nao pode ficar vazia!', 'password')
        else:
            for user in load_excel['User'].values:
                linha = load_excel[load_excel['User'] == user.lower()]
                linha_password = str(linha.iloc[0]['Password'])
                if password == linha_password:
                    # Carrega as mensagens ao acessar o chat
                    return redirect(url_for('chat'))
                else: 
                    flash('Nome de Usuario ou Senha invalido!','password')
                    return render_template('login.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    excel()
    id()
    add_registro = {}
    load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")

    if request.method == 'POST':
        user = request.form.get('username').strip()
        for letra in user:
            if letra in [' ', '.', ',', '@', '#', '*', '/', '\,', '|', '?', '$', '', '%']:
                return render_template('register.html')        
        if not user: 
            flash('O Nome de Usuario nao pode ficar vazio!', 'user')
            return render_template('register.html')
        
        elif len(user) < 5: 
            flash('O Nome de Usuario nao pode conter menos que 5 caracteres!', 'user')
            return render_template('register.html') 
        
        elif len(user) > 12:
            flash('O Nome de Usuario nao pode conter mais que 12 caracteres!', 'user')
            return render_template('register.html')
            
        else: 
            user = user#descobrir o motivo que eu criei isso!, nao tem logica aprincipio.

        gmail = request.form.get('email').strip()
        if not gmail:
            gmail = 'Nao Informado'
            add_registro = {'Gmail': gmail}

        password = request.form.get('password').strip()
        if not password:
            flash('A Senha nao pode ficar vazia!','password')
            return render_template('register.html')
        elif len(password) < 5:
            flash('A Senha nao pode conter menos que 5 caracteres!', 'password')
            return render_template('register.html')
        elif len(password) > 12:
            flash('A Senha nao pode conter mais que 5 caracteres!', 'password')
            return render_template('register.html')
        elif password == user:
            flash('A Senha nao poder ser igual o nome de Usuario!', 'password')
            return render_template('register.html')
        else: 
            password = password.lower()

        passwordconfim = request.form.get('passwordconfirm')
        if not password == passwordconfim:
             flash('A Senha nao e a mesma de cima!', 'password_confirm')
             return render_template('register.html')
        
        if user in load_excel['User'].values:
            flash('O Nome de Usuario ja existe!', 'user')
            return render_template('register.html')
        else:
            add_registro = {
                'User': user.lower(),
                'Gmail': gmail.lower(),
                'Password': password,
                'ID': ID                
            }

            load_excel = pd.concat([load_excel, pd.DataFrame([add_registro])], ignore_index=True)
            load_excel.to_excel(caminho_excel_registros, index=False, engine='openpyxl')
            return render_template('login.html')

    return render_template('register.html')


@app.route('/chat')
def chat():
    load_excel_mensagens = pd.read_excel(caminho_excel_mensagens, engine='openpyxl')
    dados = load_excel_mensagens.to_dict(orient='records')

    return render_template('chat.html', dados=dados)


def id():
    global ID
    load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")

    ID = 'id:'
    quantidade_numero_id = random.randrange(8,13)
    quantidade_id = 0
    while quantidade_numero_id > quantidade_id:
        numero_random = random.randrange(0,11)
        ID = ID + str(numero_random)
        quantidade_id += 1
    ID = 'id:69744101361066'
    if ID in load_excel['ID'].values:
        flash('Desculpe: Alguma coisa de errado aconteceu no servidor, tente-se registrar novamente.', 'password_confirm')
        return render_template('register.html')
    else:
        ID = ID


def excel():
    if os.path.exists(caminho_excel_registros): 
        load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")

    else:
        criar_excel_registros = {
            "User": [],
            "Gmail": [],
            "Password": [],
            "ID": []
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
    