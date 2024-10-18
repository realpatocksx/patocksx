from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'xss_test'

usuarios = {'admin': '12345'}  # Dados de login fixos para simular a autenticação

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in usuarios and usuarios[username] == password:
            return redirect(url_for('welcome', user=username))  # Redireciona para a página de boas-vindas
        else:
            return redirect(url_for('login_error', user=username))

    return render_template('login.html')

@app.route('/welcome/<user>')
def welcome(user):
    return render_template('welcome.html', user=user)

@app.route('/login_error')
def login_error():
    user = request.args.get('user', '')
    return render_template('login_error.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)