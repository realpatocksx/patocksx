from flask import Flask, request, render_template_string, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'xss_test'

usuarios = {'admin': '12345'}  # Dados de login fixos para simular a autenticação

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in usuarios and usuarios[username] == password:
            return redirect(url_for('welcome', user=username))
        else:
            # Redireciona para uma página de erro, exibindo o nome do usuário fornecido
            return redirect(url_for('login_error', user=username))

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Login</title>
        </head>
        <body>
            <h2>Login</h2>
            <form method="POST">
                <label>Usuário:</label><br>
                <input type="text" name="username"><br><br>
                <label>Senha:</label><br>
                <input type="password" name="password"><br><br>
                <button type="submit">Entrar</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/login_error')
def login_error():
    # Exibe o nome do usuário sem escapar, simulando uma vulnerabilidade XSS
    user = request.args.get('user', '')
    return render_template_string(f'''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Erro de Login</title>
        </head>
        <body>
            <h2>Erro de Login</h2>
            <p>O usuário <b>{user}</b> não pôde ser autenticado.</p>
            <a href="/">Voltar para o Login</a>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
    #'''
    '''
    <script>function teste(){alert('funfa')};teste()</script>
    '''