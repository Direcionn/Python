"""
Pode se ter listas dentro de listas.
"""

#Listas com colchetes
frutas = ['Maça', 'Uva', 'Laranja']

#Lista vazia
fruta = []

#Listas com o construtor 'list'
"""
Nesse caso cada letra da string será considerado um elemento da lista.
Ex. P = [0], y = [1], assim por diante

Obs. O método 'list' só pode receber um único elemento,
caso receba mais de 1 ele retornará um erro.
"""
texto = list('Python')

#Listas com a função 'range'
"""
Nesse caso cada número do range será considerado um elemento da lista.
Lembrando que o 'range' vai até o valor anterior declarado.
Ex. range(10) contêm valores de 0 á 9.
"""
numero = list(range(10))

#Listas com diferentes tipos de variaveis
"""
Exemplo de lista com diferentes tipos de variaveis.
"""
carro = ['Ferrari', 'F8', 420000, 2020, 'São Paulo']

#Listas aninhadas - Matriz
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]
print(matriz[0]) #Primeira linha inteira
print(matriz[0][1]) #Elemento 'a'
print(matriz[2][2]) #Elemento 'c'

#Fatiamento de listas
lista = list('Python')
print(lista[2:])
print(lista[1:3])
print(lista[::-1])

#Iterar listas
"""
Ele passa por cada elemento da lista e retorna ele.
"""
for elemento in frutas:
    print(elemento)

#Função enumerate
"""
Usado para saber o índice do elemento
"""
for indice, elemento in enumerate(frutas):
    print(f'{indice}: {elemento}')

#Compreensão de listas
"""
Usado para criar novas listas por meio de listas já existentes.
"""
"""
Sem a compresão
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numeros%2 == 0:
        pares.append(numero)
print(pares)
"""
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
#Ele funciona como uma função ternaria
print(pares)

"""
Modificando com a compresão
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)
"""
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

