class valor_bruto:

    def __init__(self, valor_bruto):
        self.__valor_bruto = valor_bruto


def bruto(valor):
    s=0
    for i in range (0, len(valor)):
        s=s+valor[i]
    return s
def gasto(gasto):
    s=0
    for i in range(0, len(gasto)):
        s=s+gasto[i]
    return s

def liq (b,g):
    b = bruto(valor)
    g = gasto(gasto)
    liq=b-g
    return liq

def mot (liq):
    l=liq(gasto)
    m=liq*0.3
    return m
