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
    valor_motorista = liquido * 0.3
    return valor_motorista


def pagamento_associado():
    total_associado = valor_liquido(dados) - pagamento_motorista()
    return total_associado


def km_rodados(dados):
    km_rodado = dados['kmrodados'].sum()
    return km_rodado

# total pago em combustivel na nota
# total da nota dividido pelo preço do combustível
# total de combustivel em Litros
def quantidade_de_combustivel(dados):
    combustivel = round(dados['combustivel'].sum(), 2)
    preco_combustivel = 4.19
    quantidade = combustivel / preco_combustivel
    return quantidade


def consumo():
    km_por_litro = km_rodados(dados) // quantidade_de_combustivel(dados)
    print(km_por_litro)


def valores_totais():
    print(tabulate([['Valor bruto:', valor_bruto(dados)], ['Combustível(-)', gastos(dados)],
                    ['Valor liquido', valor_liquido(dados)],
                    ['Pagamento motorista(-)', round(pagamento_motorista(), 2)],
                    ['pagamento associado', round(pagamento_associado(), 2)],
                    ['Total de KM rodados: ', (km_rodados(dados))],
                    ['Quantidade de combustível em Litros: ', (round(quantidade_de_combustivel(dados), 2))]]))


valores_totais()
km_rodados(dados)
quantidade_de_combustivel(dados)
consumo()
