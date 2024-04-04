num = int(input('Digite um numero de 0 a 20: '))
num_extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 
               'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 
               'Catoze', 'Quize', 'Dezeseis', 'Dezete', 'Dezoito', 'Dezenove', 'Vinte')

if num > 20:
    print(f'\033[0;31m' + 'ERRO: ' + '\033[0m' + f'O Numero {num} é maior que 20!. ') 
elif num < 0:
    print(f'\033[0;31m' + 'ERRO: ' + '\033[0m' + f'O Numero {num} é menor que zero!. ')
else: 
    print(f'Voce digitou o numero {num_extenso[num]}!')