'''
from datetime import date
import math

print('-----------  Consulte sua parte diária detalhada  ----------- ')

mot = int(input('Para associados, digite [1]      \nPara defensor, digite [2]: '))
if mot == 1:
    num = int(input('Jose Raimundo Barros de Araújo      \n Digite seu nº de associação: '))
    if num == 19:
        nome = ('Jose Raimundo Barros de Araújo')
        print('Acesse sua ultima parte diaria cadastrada no sistema:')
    else:
        print('Associado não cadastrado')
elif mot == 2:
    defe = input('Digite seu nome: ')
else:
    print('Inválido')
if mot == 1:
    carro = int(input('Qual o nª do carro dirigido?: '))
    if carro == 89:
        print('carro dirigido por outro motorista')
    if carro == 19:
        carro1 = ('nissan Versa')
    else:
        print('veículo não cadastrado')



    a = 0
    x = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\barros\\valor.txt', a)
    g = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\barros\\gasto.txt', a)
    k = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\barros\\kmrodados.txt', a)
    c = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\barros\\combustivel.txt', a)
    cmb = float(input('Qual o valor do combustível na nota fiscal?'))
    liq = total(x) - gasto(g)
    mot = liq * 0.3
    litros = total(c) / cmb
    kml = total(k) / litros
    if carro == 19:
        print('----------------------------------------------------------------------------------------------')
        print("total:", total(x), '//', 'gasto', gasto(g), '//', 'liquido', liq, '//', 'motorista', mot, '//',
              'km rodados', total(k), '//')
        print('Quantidade média de combustível: ', round(litros, 2), 'L', '//', 'combustível R$', round(total(c), 2),
              '//', 'consumo médio do veículo', round(kml, 2), 'Km/L')
        print('----------------------------------------------------------------------------------------------')
        print('motorista:', nome, '  \nCarro:', carro1)
        print('----------------------------------------------------------------------------------------------')
        prt = open('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\barros\\diaria.txt', 'r')
        txt = prt.read()
        print(txt)
        prt.close()
    else:
        print('Erro no veículo')

if mot == 2:
    carro = int(input('Qual o nª do carro dirigido?: '))
    if carro == 19:
        print('carro dirigido por outro motorista')
    if carro == 89:
        carro1 = ('Chevrolet Spin Lt')
    else:
        print('veículo não cadastrado')
if mot == 2:
    def total(dados):
        s = 0
        for i in range(0, len(dados)):
            s = s + dados[i]
        return s


    def gasto(gasto):
        s = 0
        for i in range(0, len(gasto)):
            s = s + gasto[i]
        return s


    def carregadados(nomearq, a):
        temp = []
        arq = open(nomearq, 'r')
        linhas = arq.readlines()
        for linha in linhas:
            temp.append(float(linha) + a)
        arq.close()
        return temp


    a = 0
    x = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\jose\\valor.txt', a)
    g = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\jose\\gasto.txt', a)
    k = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\jose\\kmrodados.txt', a)
    c = carregadados('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\jose\\combustivel.txt', a)
    cmb = float(input('Qual o valor do combustível na nota fiscal?'))

    liq = total(x) - gasto(g)
    mot = liq * 0.3
    litros = total(c) / cmb
    kml = total(k) / litros
    if carro == 89:
        print('----------------------------------------------------------------------------------------------')
        print("total:", total(x), '//', 'gasto', gasto(g), '//', 'liquido', liq, '//', 'motorista', mot, '//',
              'km rodados', total(k), '//')
        print('Quantidade média de litros: ', round(litros, 2), 'combustível', round(total(c), 2), '//',
              'consumo médio do veículo', round(kml, 2), 'Km/L')
        print('----------------------------------------------------------------------------------------------')
        print('motorista:', defe, '  \nCarro:', carro1)
        print('----------------------------------------------------------------------------------------------')
        prt = open('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho\\barros\\diaria.txt', 'r')
        txt = prt.read()
        print(txt)
        prt.close()
    else:
        print('Erro no veículo')
'''
