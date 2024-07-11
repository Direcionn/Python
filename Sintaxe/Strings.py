#Métodos da classe String
curso ="pYThoN"

print(curso.upper())
print(curso.lower())
print(curso.title())

#Eliminando espaços em branco
curso = '   Python '

print(curso.strip()) #Todos os espaços em branco
print(curso.lstrip()) #Todos os espaços em branco a esquerda
print(curso.rstrip()) #Todos os espaços em branco a direita

#Junção e centralização
curso = 'Python'

print(curso.center(10, '#'))
print('.'.join(curso))

#Formatação com f strings
nome = 'Murilo'
idade = 20
escolaridade = 'Ensino médio completo'

print(f'Olá meu nome é {nome}, tenho {idade} anos e minha escolaridade é {escolaridade}.')

#Formatação de números com f strings
PI = 3.14159
print(f'O valor de Pi é {PI:.2f}')
print(f'O valor de Pi é {PI: 2.2f}')

#Fatiamento de String
nome = 'Murilo da Silva Vieira'

print(nome[0]) #'M'
print(nome[:6]) #'Murilo'
print(nome[6:15]) #'da Silva'
print(nome[6:13:2]) #'aSl'
print(nome[:]) #String completa
print(nome[::-1]) #String inversa

#String de múltiplas linhas
nome = 'Murilo'
#Pode ser usado três apas simples ou três duplas.
#Obs. três aspas simples pode ser comentários tambem.

mensagem = f'''
Olá meu nome é {nome} e
estou aprendendo Python'''
print(mensagem)

