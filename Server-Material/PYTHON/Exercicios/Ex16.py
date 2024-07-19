soma = 0
contador = 0

for n in range(1, 501,2):
    if n % 3 == 0:
        soma = soma + n
        contador += 1 

print(f'a soma de todos os {contador} valores solicitados, é {soma}')