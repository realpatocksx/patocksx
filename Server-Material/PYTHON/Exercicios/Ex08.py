'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço 
militar, se é a hora exata de se alistar ou se já passou do tempo do 
alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
 '''

from datetime import date

ano_atual = date.today().year
idade_nascimento = int(input('Informe sua data de nacimento: '))
idade_atual = 2024 - idade_nascimento

print(f'Quem nasceu em {idade_nascimento} tem {idade_atual}anos em {ano_atual}.')

if idade_atual > 18:
    idade_inscricao = idade_atual - 18 
    inscricao = 18 + idade_nascimento
    print(f'Voce ja deveria ter se alistado ha {idade_inscricao}anos atras!. ')
    print(f'Seu alistamento foi em {inscricao}.')

elif idade_atual == 18:
    idade_inscricao = 18 - idade_atual 
    inscricao = 18 + idade_nascimento
    print('Voce tem que ser alistar IMEDITAMENTE')

else:
    idade_inscricao = 18 - idade_atual 
    inscricao = 18 + idade_nascimento
    print(f'Ainda falta {idade_inscricao}anos para o seu alistamento!. ')
    print(f'Voce podera fazer o alistamento em {inscricao}.')
