altura = float(input('Informe sua altura (m): '))
peso = float(input('Informe seu peso (Kg): '))

imc = peso / (altura * altura)
imc = imc
print(f'O seu imc é {imc:.1f}')

if imc < 18.5:
    print('Voce esta abaixo do peso!.')
    print('Começar a comer mais!!!.')

elif imc >= 18.5 and imc < 25:
    #elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal.')
    print('Parabens continue assim!.')

elif imc >= 25 and imc < 30:
    print('Voce esta acima do peso!!.')
    print('Pare de comer, esta na hora de fazer uma dieta.')

elif imc >= 30 and imc < 40:
    print('Voce esta obso.')
    print('Bora fazer uma dieta ne pai? madeira pro caixao esta caro!.')

elif imc >= 40:
    print('Voce agora esta com obsidade morbida!.')
    print('Se fudeu avisei para parar de comer, e fazer uma dieta!.')
    print('Agora so vai da despesar com caixao, fdp#@#&@!.')