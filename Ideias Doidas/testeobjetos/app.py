listadesordenada = [2, 1, 4, 5, 7, 9, 3, 8, 0, 6]

def ordenalista(lista):
    novalista = listadesordenada
    print('primeira lista', novalista)
    itematual = listadesordenada[1]
    for item in lista:
        if item > itematual:
            indice1 = item 
            indice2 = itematual
            novalista = listadesordenada[indice1], listadesordenada[indice2] = listadesordenada[indice2], listadesordenada[indice1]
            print('sim e maior',item,itematual)            
            itematual += 1
            print('Item atual era', itematual)
        elif item < itematual:
            indice1 = item 
            indice2 = itematual
            novalista = listadesordenada[indice2], listadesordenada[indice1] = listadesordenada[indice1], listadesordenada[indice2]
            print('nao e maior',item,itematual)
            itematual -= 1
            print('Item atual era', itematual)
            

    print(novalista)
ordenalista(listadesordenada) 













'''
listadesordenada = [2, 1, 4, 5, 7, 9, 3, 8, 0, 6]

def ordenalista(lista):
    n = len(lista)
    # Percorre a lista várias vezes
    for i in range(n):
        # Em cada iteração, percorre os elementos restantes
        for j in range(0, n - i - 1):
            # Se o elemento atual é maior que o próximo, troca-os
            print('teste 1', lista[j])
            print('teste 2',lista[j + 1])
            print(lista)
    
    return lista

lista_ordenada = ordenalista(listadesordenada)
print("Lista ordenada:", lista_ordenada)'''