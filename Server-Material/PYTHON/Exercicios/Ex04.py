numero = int(input('Informe um numero do tipo inteiro: '))
formular_impar_par = numero % 2

if formular_impar_par == 0:
    print(f'O numero que voce digitou: {numero} é PAR!')
else:
    print(f'O numero que voce digitou: {numero} é IMPAR!')