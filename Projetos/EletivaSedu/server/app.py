from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.abspath('Projetos/EletivaSedu/client/'), static_folder=os.path.abspath('Projetos/EletivaSedu/client/')) 

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')

if __name__ == '__main__':
    app.run(debug=True)
