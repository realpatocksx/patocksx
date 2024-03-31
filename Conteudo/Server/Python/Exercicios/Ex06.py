def conversorbases():

    numero = int(input('Informe um numero inteiro: '))

    print('''ESCOLHAR UM TIPO DE CONVERSO
[ 1 ] Binario 
[ 2 ] Octal 
[ 3 ] Hexadecimal''')
    
    categoria = int(input('Informa a base que desejar fazer a conversao: '))

    if categoria == 1:
        print(f'O {numero} convertido para Binario é {bin(numero)[2:]}')

    elif categoria == 2: 
        print(f'O {numero} convertido para Octal é {oct(numero)[2:]}')

    elif categoria == 3:
        print(f'O {numero} convertido para Hexadecimal é {hex(numero)[2:]}')
    else:
        print('\033[0;31m' + 'ERRO:' + '\033[0m' + ' Voce nao digitou nenhuma das opcoes acima!')
conversorbases()