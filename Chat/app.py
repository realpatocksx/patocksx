from flask import Flask, render_template, request, redirect, url_for
import os, pandas as pd

app = Flask(__name__)

@app.route('/')
def inicio():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    excel()
    load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")

    user = request.form.get('username')
    password = request.form.get('password')
    verificar_user = user in load_excel['User'].values
    linha = load_excel[load_excel['User'] == user]
  
    if verificar_user:
        if not linha.empty:
            linha_gmail = linha.iloc[0]['Gmail']
            linha_password = linha.iloc[0]['Password']
            print(password)
            print(linha_password)
            if password == linha_password:
                print('teste', linha_password)
                print('teset', password)
                return render_template('chat.html')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    excel()
    load_excel = pd.read_excel(caminho_excel_registros, engine="openpyxl")

    user = request.form.get('username')
    gmail = request.form.get('email')
    password = request.form.get('password')

    add_registro = {
        'User': user,
        'Gmail': gmail,
        'Password': password
    }

    load_excel = pd.concat([load_excel, pd.DataFrame([add_registro])], ignore_index=True)
    load_excel.to_excel(caminho_excel_registros, index=False, engine='openpyxl')
    print('add sucessu')
    return render_template('register.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')

caminho_excel_registros = 'Chat/static/data/registros.xlsx'
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
        

if __name__ == '__main__':
    app.run(debug=True)


'''
# Filtrar o DataFrame para encontrar a linha correspondente
linha = df[df['User'] == nome]

# Verificar se encontrou alguma linha
if not linha.empty:
    # Obter o Gmail e Password da linha filtrada
    #gmail = linha.iloc[0]['Gmail']  # Obtém o Gmail da primeira (e única) linha
    #password = linha.iloc[0]['Password']  # Obtém a senha da primeira (e única) linha
    
'''