from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar dados do Excel
def load_users():
    df = pd.read_excel('Chat/static/data/registros.xlsx')  # Altere para o caminho do seu arquivo
    return df['User'].tolist()  # Supondo que a coluna que você quer é chamada 'nome'

@app.route('/')
def index():
    return render_template('estuda.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    users = load_users()
    filtered_users = [user for user in users if query in user.lower()]
    print('teste')
    print(users)
    print(query)
    return jsonify(filtered_users)

if __name__ == '__main__':
    app.run(debug=True)
