import pandas as pd
from tabulate import tabulate
diaria_jose = "https://raw.githubusercontent.com/georgematheuslima/projeto-aeroporto/master/jose/diaria.txt"
diaria_barros = "https://raw.githubusercontent.com/georgematheuslima/projeto-aeroporto/master/barros/diaria.txt"
dados = pd.read_csv(diaria_jose)
print(dados)

def valor_bruto(dados):
    valor_total = dados['valor'].sum()
    return valor_total

def gastos(dados):
    despesas = dados['combustivel'].sum()
    return despesas

def valor_liquido(dados):
    valor_total = dados['valor'].sum()
    despesas = dados['combustivel'].sum()
    valor_livre = valor_total - despesas
    return valor_livre

def pagamento_motorista():
    liquido = valor_liquido(dados)
    pagamento_motorista = liquido *0.3
    return pagamento_motorista


def pagamento_associado():
    total_associado = valor_liquido(dados) - pagamento_motorista()
    return total_associado


def valores_totais():
    print(tabulate([['Valor bruto:', valor_bruto(dados)], ['Gastos', gastos(dados)],
                    ['Valor liquido', valor_liquido(dados)], ['Pagamento motorista', round(pagamento_motorista(), 2)],
                    ['pagamento associado', round(pagamento_associado(), 2)]]))



valores_totais()

