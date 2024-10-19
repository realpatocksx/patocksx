from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

usuarios = {
    'admin': '123',
    'pedro': '123456'
    }  

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')#pedro
        password = request.form.get('password')

        if username in usuarios and usuarios[username] == password:
            return redirect(url_for('welcome', user=username))  
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




