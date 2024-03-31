from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/pesquisar', methods=['GET'])
def dadosducksxnome():
    nome = request.args.get('nome', '')
    nome_formatado = nome.replace(' ', '+')
    url = f"https://dbftools.pro/api/tools/name?q={nome_formatado}"
    dados = requests.get(url)
    
    if dados.status_code == 200:
        return jsonify(dados.json())
    else:
        return jsonify({'error': 'API não está funcionando'}), 500
    
if __name__ == '__main__':
    app.run(debug=True)

