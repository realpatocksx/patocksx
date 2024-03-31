import pandas as pd

def login():
    print('funfa')
    df = pd.read_excel('Projetos/Flask/server/inscricoes.xlsx')

    # Obtém o valor da terceira célula da coluna A
    valor_A3 = df.iloc[2, 0]
    print(valor_A3)
login()