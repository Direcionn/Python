#Dicionários 
"""
É um conjunto não-ordenado de pares chave: valor, onde as chaves são únicas para cada valor
Eles são delimitados por chave:{} e contêm uma lista de pares chave: valor separadas por vírgulas.
"""
pessoa = {'nome': 'Murilo', 'idade':20 } #Uma forma de ser declarado
print(pessoa)
pessoa = dict(nome = 'Murilo', idade = 20) #Outra forma de ser declarado
print(pessoa)
pessoa['telefone'] = '3333-1234'
print(pessoa)

#Acesso aos dados
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

pessoa['nome'] = 'Maria'
pessoa['idade'] = 18
pessoa['telefone'] = '9988-1781'
print(pessoa)

#Dicionários aninhadas - Pode armazenar qualquer tipo de dado, desde que a chave seja imutável
contatos ={
    'murilo@gmail.com': {'nome': 'Murilo', 'telefone': '3333-1234'},
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3334-5678'},
    'eduardo@gmail.com': {'nome': 'Eduardo', 'telefone': '3335-9012'},
    'renan@gmail.com': {'nome': 'Renan', 'telefone': '3336-3456'}
}
print(contatos)

print(contatos['eduardo@gmail.com']['telefone'])
print(contatos['guilherme@gmail.com']['nome'])

#Iterar dicionários - Da mesma forma de listas e afins
"""
for chave in contatos:
    print(chave, contatos[chave])

Não é a forma mais correta, pois fica dificil a leitura dos dados
"""
for chave, valor in contatos.items(): #Forma mais correta de se interar um dicionário
    print(chave, valor)

