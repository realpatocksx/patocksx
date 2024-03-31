import random 
import time 


#lista_numeros = ['0', '1', '2', '3', '4', '5'] foma errada

#numero_aleatorio = int(random.choice(lista_numeros)) forma errada

computador = random.randint(0,5)

print('Aguarde...\nPensando em um numero!')
time.sleep(1)
jogador = int(input('Tente adivinha qual o numero que o computador pensou?'))
print('PROCESSANDO')
time.sleep(1)


if jogador == computador:
    print(f'Voce acertou, pois o numero que o computador pensou foi {computador}')
else:
    print(f'Voce errou, pois o numero que o computador pensou foi {computador}')
