# Exercicios Especial 01

import random

def forca():
    comida = ['arroz', 'feijao', 'carne']
    carro = ['bmw', 'ford', 'ferrari']
    pais = ['canada', 'suica', 'grecia']
    
    tudo = comida + carro + pais

    palavra = random.choice(tudo)

    vida_inicial = 5 
    acerta = True

    while acerta:
        print(palavra)
        tentativa = str(input('Digite a palavra que acha que é: '))

        if tentativa == palavra:
            print(f'Sucesso voce acertou a palavra era {palavra}')
            acerta = False
        else:
            print('Voce errou! mas tem mais tentativas.')
            
forca()