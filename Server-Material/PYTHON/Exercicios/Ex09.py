reta1 = float(input('Informe o primeiro segmento: '))
reta2 = float(input('Informe o segundo segmento: '))
reta3 = float(input('Informe o terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print(f'Os segmentos acima ser formam um TRIANGULO.')
else:
    print(f'Os segmentos acima nao pode forma um TRIANGULO.')
