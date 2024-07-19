reta1 = float(input('Informe o primeiro segmento: '))
reta2 = float(input('Informe o segundo segmento: '))
reta3 = float(input('Informe o terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print(f'Os segmentos acima ser formam um TRIANGULO.')

    if reta1 == reta2 and reta2 == reta3:
        print('O triangulo é EQUILATERO!.')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('O triangulo é ISOSCELES!.')
    elif reta1 != reta2 and reta2 != reta3:
        print('O triangulo é ESCALENO!.')

else:
    print('\033[0;31m' + 'ERRO:' + '\033[0m' + 'Os segmentos acima nao pode forma um TRIANGULO.')
