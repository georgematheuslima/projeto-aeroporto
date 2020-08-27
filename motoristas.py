# mot = int(input('Para associados, digite [1]      \nPara defensor, digite [2]: '))
# if mot == 1:
#     num = int(input('Jose Raimundo Barros de Araújo      \n Digite seu nº de associação: '))
#     if num == 19:
#         nome = ('Jose Raimundo Barros de Araújo')
#         print('Acesse sua ultima parte diaria cadastrada no sistema:')
#     else:
#         print('Associado não cadastrado')
# elif mot == 2:
#     defe = input('Digite seu nome: ')
# else:
#     print('Inválido')
# if mot == 1:
#     carro = int(input('Qual o nª do carro dirigido?: '))
#     if carro == 89:
#         print('carro dirigido por outro motorista')
#     if carro == 19:
#         carro1 = ('nissan Versa')
#     else:
#         print('veículo não cadastrado')


class Motorista:

    def __init__(self, associado, defensor, carro):
        self.associado = associado
        self.defensor = defensor
        self.carro = carro

    def acesso_ao_sistema(self, numero):
        if numero == 0:
            print('Associado. Digite o número de identificação do Associado:')
            identificacao = 19
            if identificacao == 19:
                print('Associado identificado: José Raimundo Barros de Araújo')
            else:
                raise ValueError ('Associado não identificado pelo sistema.')
        elif numero == 1:
            print('Defensor. Digite o Seu nome de acordo com a parte diária:')
            identificacao = str(input())
            if identificacao == 'josé viana'.upper():
                print('Defensor identificado: José Viana')
            else:
                raise ValueError ('Defensor não cadastrado no sistema.')
        else:
            raise ValueError ('Código não registrado')
