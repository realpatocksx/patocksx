# Exercicios Especial 01

import random

def forca():
    comida = ['arroz', 'feijao', 'carne']
    carro = ['bmw', 'ford', 'ferrari']
    pais = ['canada', 'suica', 'grecia']
    
    tudo = comida + carro + pais

    acerta = True
    print('ESCOLHA DE CATEGORIA\n 1- Comidas\n 2- Carros\n 3- Pais\n 4- Aleatorio\n 5- Tudo')
    categoria = int(input('Informe o numero da categoria que voce quer jogar: '))

    if categoria == 1:
        palavra = random.choice(comida)
    elif categoria == 2:
        palavra = random.choice(carro)
    elif categoria == 3:
        palavra = random.choice(pais)
    elif categoria == 4:
        print('embreve')
    elif categoria == 5:
        palavra = random.choice(tudo)
    else: 
        print('Voce nao escolheu nenhuma das opcoes acima, logo o jogo foi encerrado!')
        acerta = False

    while acerta:
        tentativa = str(input('Digite a palavra que acha que é: '))
        if tentativa == palavra:
            print(f'Sucesso voce acertou, a palavra era {palavra}')
            continua = [str(input('Se desejar continua digite [S/s]. Se nao desejar continua digite enter: '))]
            if continua == ['S']:
                print('Jogo sendo reiniciado!')
                acerta = False
                forca()
            else:
                print('Jogo sendo fechado')
                acerta = False
        else:
            print('Voce errou! mas tem mais tentativas.')
            
forca()