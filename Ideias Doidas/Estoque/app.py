from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("carrinho.html")

@app.route("/produtos")
def produtos():
    return render_template("produto.html")

@app.route("/carrinho")
def carrinho():
    return render_template("templates/carrinho.html")

@app.route("/login")
def login():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)