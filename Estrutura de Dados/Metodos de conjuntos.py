#Union - Usado para unir dois conjuntos
numeros_a = {1, 2, 3, 4}
numeros_b = {2, 3, 4, 5, 8}

print(numeros_a.union(numeros_b))

#Intersection - Usado para pegar os elementos em comum entre dois conjuntos
print(numeros_a.intersection(numeros_b))

#Diference - Usado para pegar os elementos diferentes entre dois conjuntos
print(numeros_a.difference(numeros_b))
print(numeros_b.difference(numeros_a))

#Symetric_difference - Usado para juntar elementos diferentes entre dois conjuntos
print(numeros_a.symmetric_difference(numeros_b))

#Issubset - Usado para saber se os elementos de um conjunto pertencem a outro conjunto
numeros_a = {1, 2, 3, 4}
numeros_b = {1, 2, 3, 4, 5, 6, 7, 8}

#O conjunto 'a' é subconjunto do conjunto 'b'
print(numeros_a.issubset(numeros_b)) #True

#Issuperset - Faz a mesma pergunta do de cima mas ao contrario
print(numeros_a.issuperset(numeros_b)) #False

#Isdisjoint - Usado para saber se todos os elementos de um conjunto não pertencem a outro conjunto
nomes_a = {'Adriana', 'Bruna', 'Carlos'}
nomes_b = {'Daniel', 'Eduardo', 'Felipe'}
nomes_c = {'Adriana', 'Daniel', 'Felipe'}

print(nomes_a.isdisjoint(nomes_b)) #True
print(nomes_a.isdisjoint(nomes_c)) #False
print(nomes_b.isdisjoint(nomes_c)) #False

#Add - Usado para adicionar elementos a um conjunto
#Caso já exista ele não irá adicionar
frutas = {'Abacaxi', 'Banana'}

frutas.add('Caqui')
print(frutas)
frutas.add('Damasco')
print(frutas)
frutas.add('Banana')
print(frutas)

#Clear - Usado para limpar um conjunto
nomes_c.clear()
print(nomes_c)

#Copy - Usado para copiar uma lista
vitamina_fruta = frutas.copy()
print(vitamina_fruta)

#Discard - Usado para discartar um elemento de um conjunto
#Caso o elemento não exista ele nada fará com o programa
numeros = {1,2,3,4,5,1,8,9,2,3,4,5,7}
print(numeros)

numeros.discard(1)
print(numeros)
numeros.discard(5)
print(numeros)
numeros.discard(10)
print(numeros)

#Pop - Usado para parecer com uma pilha
print(numeros.pop()) #Removerá o primeiro elemento da lista - Atual: 2
print(numeros)
print(numeros.pop()) #Atual: 3
print(numeros)

#Remove - Usado para remover um elemento em especifico
numeros_c = {1,2,3,4,5,6,1,8}
print(numeros_c.remove(2))
print(numeros_c)

#Len - Usado para saber o tamanho do conjunto
print(len(numeros_c))

#In - Usado para verificar se um elemento está no conjunto
print(1 in numeros_c) #True
print(9 in numeros_c) #False

