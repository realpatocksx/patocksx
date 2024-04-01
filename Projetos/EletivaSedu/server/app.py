from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath('Projetos/EletivaSedu/client'), static_folder=os.path.abspath('Projetos/EletivaSedu/client')) 

titulo = 'Teste da Sucao da segundo quinta'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html', Titulo=titulo)

@app.route('/secao/index.html')
def secao():
    return render_template('secao/index.html', Titulo1=titulo)

if __name__ == '__main__':
    app.run(debug=True)
