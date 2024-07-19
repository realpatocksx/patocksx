import random
import time 

print('''ESCOLHA UMA DAS OPCOES ABAIXO!
      
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA
''')

opcao_jogador = int(input('Informe qual voce quer jogar: '))
opcao_computador = random.randint(1,3)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(0.5)
print('PO')

if opcao_jogador == 1:
    print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)
    print('VOCE ESCOLHEU: PEDRA')

    if opcao_computador == 1:
        print('COMPUTADOR ESCOLHEU: PEDRA')
        print('PARTIDA: EMPATE!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

    elif opcao_computador == 2:
        print('COMPUTADOR ESCOLHEU: PAPEL')
        print('PARTIDA: COMPUTADOR GANHOU!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

    elif opcao_computador == 3:
        print('COMPUTADOR ESCOLHEU: TESOURA')
        print('PARTIDA: VOCE GANHOU!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

elif opcao_jogador == 2:
    print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)
    print('VOCE ESCONHEU: PAPEL')

    if opcao_computador == 1:
        print('COMPUTADOR ESCOLHEU: PEDRA')
        print('PARTIDA: VOCE GANHOU!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

    elif opcao_computador == 2:
        print('COMPUTADOR ESCOLHEU: PAPEL')
        print('PARTIDA: EMPATE!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

    elif opcao_computador == 3:
        print('COMPUTADOR ESCOLHEU: TESOURA')
        print('PARTIDA: COMPUTADOR GANHOU!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

elif opcao_jogador == 3:
    print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)
    print('VOCE ESCONHEU: TESOURA')
    
    if opcao_computador == 1:
        print('COMPUTADOR ESCOLHEU: PEDRA')
        print('PARTIDA: COMPUTADOR GANHOU!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

    elif opcao_computador == 2:
        print('COMPUTADOR ESCOLHEU: PAPEL')
        print('PARIDA: VOCE GANHOU!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

    elif opcao_computador == 3: 
        print('COMPUTADOR ESCOLHEU: TESOURA')
        print('PARTIDA: EMPATE!')
        print('-=-' * 10 +  'RESULTADO' + '-=-' * 10)

else: 
    print(f'\033[0;31m' + 'ERRO: ' + '\033[0m' + 'Voce nao digitou nenhuma das opcoes acima.')
    print(f'\033[0;31m' + 'ERRO: ' + '\033[0m' + 'Tente Novamente!.')
    
