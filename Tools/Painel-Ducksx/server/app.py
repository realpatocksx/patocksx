from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__, template_folder=os.path.abspath('Tools/Painel-Ducksx/client'), static_folder=os.path.abspath('Tools/Painel-Ducksx/client'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome_formatado = request.form['nome']
        opcao = request.form['opcao']
        cnpj = nome_formatado
        if opcao in ['1', '5', '6']:
            url = f"https://dbftools.pro/api/tools/name?q={nome_formatado}"
        elif opcao in ['2', '3']: 
            url = f"https://dbftools.pro/api/tools/search-cpf/{cnpj}"
        else:
            return "Em Desenvolvimento."

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            if opcao == '1':
                formatted_data = [{
                    'nome': item.get('nome'),
                    'cpf': item.get('cpf'),
                    'idade': item.get('idade'),
                    'nomeMae': item.get('nomeMae')
                    } for item in data]
                return render_template('result.html', data=formatted_data)
            elif opcao == '2':
                enderecos_formatados = []
                for endereco in data.get('enderecos', []):
                    endereco_formatado = f"{endereco.get('endereco', '')}, {endereco.get('numero', '')} - {endereco.get('bairro', '')}, {endereco.get('cidade', '')}, {endereco.get('estadoUF', '')}"
                    enderecos_formatados.append(endereco_formatado)

                emails_formatados = []
                for email in data.get('emails', []):
                    email_formatado = f"{email.get('email', '')} - {email.get('status', '')}"
                    emails_formatados.append(email_formatado)

                telefones_formatados = []
                for telefone in data.get('telefones', []):
                    telefone_formatado = f"({telefone.get('ddd', '')}) {telefone.get('numero', '')}"
                    telefones_formatados.append(telefone_formatado)

                return render_template('resultcpf.html', data=data, enderecos=enderecos_formatados, emails=emails_formatados, telefones=telefones_formatados)
        elif opcao == '3':
            return response.json(), print(response.json())
        else:
            return "ERRO: Parece que algo deu errado!."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

