numeros=[]

qtd = int(input('quantos numeros?'))
arquivo = open('C:\\Users\\geoor\\OneDrive\\Área de Trabalho\\trabalho','w')
for i in range(1 ,qtd+1):
    s = input('Digite um nome:')
    numeros.append(s)
    numeros.append('\n')
arquivo.writelines(nomes)
arquivo.close()
