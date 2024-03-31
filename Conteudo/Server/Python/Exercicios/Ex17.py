valor = float(input('Digite o numero para multiplicar: '))
print('-' * 35)
print(f'        A tabuada do {valor} é: \n'.upper())

for n in range(1,11):
    print(f'{valor} x {n} = {valor*n}')

print('-' * 35)