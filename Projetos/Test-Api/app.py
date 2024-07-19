import requests 

def dadosducksxnome():
    nome = input('Digite o nome da pesquisar: ')
    nome_formatado = nome.replace(' ', '+')
    url = f"https://dbftools.pro/api/tools/name?q={nome_formatado}"
    dados = requests.get(url)
    
    if dados.status_code == 200:
        print(dados.json())
    else: 
        print('api nao esta funcionando')
dadosducksxnome()

print('A funcao acabou')