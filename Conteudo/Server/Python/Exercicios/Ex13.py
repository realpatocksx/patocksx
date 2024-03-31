#Syntax basica
#for elemento_da_sequencia in sequencia:
#    print(elemento_da_sequencia)

#For por uma sequencia 
frutas = ['melancia', 'goiaba', 'manga', 'banada', 'abacaxi']

for fruta in frutas:
    print(fruta)

#For pegando o indice da sequencia, Usando enumerate
frutas = ['melancia', 'goiaba', 'manga', 'banada', 'abacaxi']
for indice, fruta in enumerate(frutas):
    print(f'Indice: {indice} da Fruta: {fruta}')

#For usando variais listas com o zip
frutas = ['melancia', 'goiaba', 'manga', 'banada', 'abacaxi']
pais = ['canada', 'italia', 'suica', 'grecia', 'portugal']
for fruta, pais in zip(frutas,pais):
    print(f'Fruta: {fruta} > Pais: {pais}')

#For de numero com inicio, fim e passo opcinal, Usando range
for n in range(0,10,1):
    print(n)

#For por dicionario 
dici = {"colete": 2, "agua": 5, "hamburguer": 3, "celular": 1, "lanterna": 1}

for item,valor in dici.items():
    print(f'Nome Item: {item} Valor: {valor}')