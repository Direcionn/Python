#Tupla - Quase igual a lista, mas ela é imutável
"""
A forma como se declara é colocando uma vírgula antes no fechamento do parenteses.
Ou colocando a classe 'tuple' antes das "constantes" 
"""
frutas = ('laranja', 'uva', 'maça',)
letra = tuple('Python')
numeros = ([1, 2, 3, 4])
pais = ('Brasil',)
print(numeros)

#Acesso de dados - Igual ao acesso nas listas
print(frutas[0])
print(numeros[2])

#Tuplas aninhadas - Matriz
matriz = (
    (1, 2, 'a'),
    (3, 'b', 'c'),
    (4, 'd', 5)
)
print(matriz)
print(matriz[0][2])

#Fatiamento - Igual ao modo de uso em listas
tupla = tuple('Python')
print(tupla[2:])
print(tupla[:2])
print(tupla[::-1])

#Iterar tuplas - Igual em listas, utilizando o 'for'
for elemento in frutas:
    print(elemento)

