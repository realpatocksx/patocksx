'''
esse foi o primeiro jogo da forca que fiz, a logica esta horrivel, 
mas salvei para ve minhas evolucao, e entender as merddas que estava fazendo 
'''

print('Jogo da Forca PATOCKSX!')

começar = input('Digite "jogar" para começar: ')

def forca():
    loopforca = True
    
    while loopforca:

        if começar == "jogar":
            print('ESCOLHA A CATEGORIA!')
            print(' 1 | Comidas\n 2 | frutas\n 3 | Animais\n 4 | Carro\n 5 | País\n 6 | Aleatorio\n 7 | Tudo\n 8 | Fechar')
            Comidas = ['arroz', 'churrasco', 'jeijão']
            Frutas = ['morango', 'uva', 'manga']
            Animais = ['gato', 'cachorro', 'rato']
            Carro = ['bmw', 'ferrari', 'ford']
            categoria = int(input('Digitar o numero da categoria:'))
            
            if categoria == 1:
                print('1')

            if categoria == 2:
                print('2')

            if categoria == 3:
                print('3')

            if categoria == 4:
                print('4')

            if categoria == 5:
                print('5')

            if categoria == 6:
                print('6')

            if categoria == 7:
                print('7')

            if categoria == 8:
                loopforca = False


print('o jogo acabou')

forca()


