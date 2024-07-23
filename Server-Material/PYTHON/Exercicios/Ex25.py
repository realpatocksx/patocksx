import random

def votacao_eleicao(nome_eleito1, nome_eleito2, nome_eleito3):    
    maxvotacao = 7
    voto_eleito1 = 0
    voto_eleito2 = 0
    voto_eleito3 = 0

    while voto_eleito1 + voto_eleito2 + voto_eleito3 < maxvotacao:            
        eleitores = ['voto_eleito1', 'voto_eleito2', 'voto_eleito3']
        votaocao_aleatoria = random.choice(eleitores)

        if votaocao_aleatoria == 'voto_eleito1':
            voto_eleito1 += 1
        elif votaocao_aleatoria == 'voto_eleito2':
            voto_eleito2 += 1
        else: voto_eleito3 += 1

    print(f"{nome_eleito1}: {voto_eleito1}")
    print(f"{nome_eleito2}: {voto_eleito2}")
    print(f"{nome_eleito3}: {voto_eleito3}")


    if voto_eleito1 > voto_eleito2 and voto_eleito1 > voto_eleito3:
        print(f'O {nome_eleito1} é o mais novo eleito com {voto_eleito1} votos')
    elif voto_eleito2 > voto_eleito1 and voto_eleito2 > voto_eleito3:
        print(f'O {nome_eleito2} é o mais novo eleito com {voto_eleito2} votos')
    elif voto_eleito3 > voto_eleito1 and voto_eleito3 > voto_eleito2:
        print(f'O {nome_eleito3} é o mais novo eleito com {voto_eleito3} votos')

nome1 = input('Informe o nome do eleitor: ')
nome2 = input('Informe o nome do eleitor: ')
nome3 = input('Informe o nome do eleitor: ')
votacao_eleicao(nome1, nome2, nome3)