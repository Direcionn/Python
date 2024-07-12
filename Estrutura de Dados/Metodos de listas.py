#Append - Usado para adicionar elementos as listas
lista = []
lista.append(1)
lista.append("Python")
print(lista)

#Clear - Usado para limpar os elementos da lista
lista.clear()
print(lista)

#Copy - Usada para copiar uma lista. Não são modificadas ao mesmo tempo
l2 = lista.copy()
print(l2)
"""
Usado o método 'id' para verificar a localidade de cada variavel.
"""
print(id(l2))
print(id(lista))

#Count - Usado para contar quantas vezes um elemento foi repetido na lista
cores = ['azul', 'amarelo', 'verde', 'azul', 'vermelho']
print(cores.count('azul'))
print(cores.count('verde'))
print(cores.count('preto'))

#Extend - Usado para adicionar 2 ou mais elementos em uma lista já existente
linguagens = ['c', 'java', 'js']
print(linguagens)
linguagens.extend(['python', 'csharp', 'ruby'])
print(linguagens)

#Index - Usado para descobrir o indice da primeira ocorrencia de determinado elemento
print(linguagens.index('c'))
print(linguagens.index('java'))

#Pop - Semelhante a pilha, vai seguinte do último elemento em diante
"""
Pode ser usado indice para saber uma posição em especifico.
"""
print(linguagens.pop()) # ruby
print(linguagens.pop()) # csharp
print(linguagens.pop(0)) # c

#Remove - Uma forma de se remover determinado elemento
linguagens.remove('js')
print(linguagens)
linguagens.extend(['java', 'java', 'c'])
print(linguagens)
linguagens.remove('java')
print(linguagens)

#Reverse - Usado para inverter a ordem dos elementos da lista
nome = ['Murilo', 'Giovanne', 'Claudia', 'Eduardo', 'Renan', 'Luiza']
nome.reverse()
print(nome)

#Sort - Usado para ordnar uma lista
linguagens.sort() #Ordenação em ordem alfabetica
print(linguagens)
linguagens.sort(reverse = True) #Ordenação de forma de z á a
print(linguagens)
linguagens.sort(key = lambda x: len(x)) #Ordenação de pelo tamanho das palavras (crescente)
print(linguagens)
linguagens.sort(key = lambda x: len(x), reverse = True) #Ordenação de forma decrecente pelo tamanho da palavra
print(linguagens)

#Len - Usado para saber o tamanho da lista
print(len(nome))

#Sorted - Igual ao sort, a unica diferença é que ele é uma função built-in do Python

