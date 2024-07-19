num = float(input('Digite o primeiro numero: '))
num2 = float(input('Digtte o segundo numero: '))

if num > num2:
    print(f' {num:.2f} é maior {num2:.2f}')
elif num < num2:
    print(f'{num:.2f} é menor de {num2:.2f}')
else:
    print(f'{num:.2f} é {num2:.2f} sao iguais! ')