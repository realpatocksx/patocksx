from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath('Projetos/EletivaSedu/client/'), static_folder=os.path.abspath('Projetos/EletivaSedu/client/')) 

@app.route('/', methods=['GET', 'POST'])
def index():
    titulo = 'Teste da Sucao da segundo quinta'
    return render_template('main/index.html', Titulo=titulo)

if __name__ == '__main__':
    app.run(debug=True)
