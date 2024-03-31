soma = 0

for soma_pares in range(1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n 
        
print(f'A soma de todos os numeros pares é {soma}')