import random

def votacao_eleicao(nome_eleito1, nome_eleito2, nome_eleito3):
    print('')
    
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

print(f"voto_eleito1: {voto_eleito1}")
print(f"voto_eleito2: {voto_eleito2}")
print(f"voto_eleito3: {voto_eleito3}")