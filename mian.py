listadesordenada = [2,0,4,5,7,9,3,8,1,6]

def ordenalista(lista):
    novalista = []
    itematual = listadesordenada[1]
    for item in lista:
        if item > itematual:
            indice1 = item 
            indice2 = itematual
            novalista = listadesordenada[indice1], listadesordenada[indice2] = listadesordenada[indice2], listadesordenada[indice1]
            print('sim e maior',item,itematual)            
        elif item < itematual:
            indice1 = item 
            indice2 = itematual
            novalista = listadesordenada[indice2], listadesordenada[indice1] = listadesordenada[indice1], listadesordenada[indice2]
            print('nao e maior',item,itematual)

    print(novalista)
ordenalista(listadesordenada)        
