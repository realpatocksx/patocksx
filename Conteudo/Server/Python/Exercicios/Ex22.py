num = int(input('Informe um numero: ')), int(input('Informe um numero: ')), int(input('Informe um numero: ')), int(input('Informe um numero: '))

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na posisao {num.index(3)+1}') 
else: print('O valor 3 não foi informado')

print(f'Os Valores pares são: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=', ')
