valor_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salario: R$'))
anos = int(input('Informe em quantos anos desejar pagar o emprestimo: '))
prestacao = valor_casa / (anos * 12)
minimo = (prestacao * 30) / 100

print('\n \033[0;35m' + '-=-' * 35 + '\033[\n')

print(f' Para pagar a casa de R${valor_casa:.2f} em {anos}anos o emprestismo sera R${prestacao:.2f}\n')

print('\033[0;35m' + '-=-' * 35 + '\033[0m\n')

if prestacao <= minimo:
    print('Emprestimo foi CONCEDIDO')
else:
    print('Emprestimo foi NEGADO')