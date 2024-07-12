#Conjuntos - Uma forma de não ter duplicatas em listas
numeros = [1, 2, 3, 1, 3, 4]
fruta = list('abacaxi')
carros = ['palio', 'gol', 'celta', 'palio']

print(set(numeros))
print(set(fruta))
print(set(carros))

#Acesso de dados - Não suporta indexação e fatiamento
"""
Para acessar os dados será necessário converter o conjunto em uma lista
"""
nomes = {'Murilo', 'Giovanne', 'Eduardo', 'Luiza', 'Renan', 'Eduardo'}
nomes = list(nomes)
print(nomes)
print(nomes[1])

#Iterar conjuntos - A sintaxe é a mesma de listas e tuplas
nomes = {'Murilo', 'Giovanne', 'Eduardo', 'Luiza', 'Renan', 'Eduardo'}
for nome in nomes:
    print(f'O nome é {nome}')

#Função enumerate - Usado para saber o indice no laço 'for'. Sintaxe igual em listas
for indice, nome in enumerate(nomes):
    print(f'{indice}: {nome}')



