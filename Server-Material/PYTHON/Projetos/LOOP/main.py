#CRIANDO UM LOOP SEM USA UM LOOP

def loop_while_original():
    valor_inicial_loop = 0
    valor_final_loop = 10
    while valor_inicial_loop < valor_final_loop:
        valor_inicial_loop = valor_inicial_loop + 1
        print(valor_inicial_loop)

'''
vn = valor inicial
vf = valor final
'''
def enquanto(vn, vf):

    
    if vn <= vf:
        print(vn)
        vn += 1
        enquanto(vn, vf)
    else:
        return print('LOOP: FIM')

enquanto(0, 5)
