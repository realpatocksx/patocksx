import requests 

numero_tell =  int(input('Informe o numero de telefone: '))

url = f"https://dbftools.pro/api/tools/phone?q={numero_tell}"

response = requests.get(url)
#27998140296
if response.status_code == 200: 
    print(response.json())  
else:  
    print('A api nao esta online! Tenta novamento mais tarde. ')
    