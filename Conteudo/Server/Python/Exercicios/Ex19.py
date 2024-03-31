
ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = ptermo + (10-1) * razao

for pa in range(ptermo, decimo + razao, razao):
    print(pa, '', end='')
print('Acabou')