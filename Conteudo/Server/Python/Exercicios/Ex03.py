velocidade = float(input('Qual e a velocidade do carro: '))
velocidade_max = 80
multa = (velocidade - velocidade_max) * 7

if velocidade > velocidade_max:
    print(f'Voce levou uma multado de R${multa}reais\nPois passou do limite de 80km/h, Voce estava a {velocidade}Km/h')
elif velocidade == velocidade_max:
    print(f'Voce esta no limite da velocidade maxima de 80km/h, mas o gerente esta maluco e decidiu nao te multa dessa vez!')
else:
    print(f'voce esta abaixo do limite maximo parabens, voce esta a {velocidade}km/h')
    print('Gracas a isso voce ganhou um bonus de 5pontos na Detran-Br')
