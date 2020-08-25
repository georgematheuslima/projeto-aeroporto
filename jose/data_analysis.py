import pandas as pd

dados = open("/home/george/Área de Trabalho/matheus/projeto aeroporto atualizado/jose", 'r')

data = pd.read_csv(dados, error_bad_lines=False)
print(data)
