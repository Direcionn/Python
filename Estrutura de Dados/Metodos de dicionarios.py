#Clear - Usado para limpar o dicionário
contatos ={
    'murilo@gmail.com': {'nome': 'Murilo', 'telefone': '3333-1234'},
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3334-5678'},
    'eduardo@gmail.com': {'nome': 'Eduardo', 'telefone': '3335-9012'},
    'renan@gmail.com': {'nome': 'Renan', 'telefone': '3336-3456'}
}
contatos_copia = contatos.copy()
contatos.clear()
print(contatos)

#Copy - Usado para criar uma cópia de um dicionário
contatos_copia_1 = contatos.copy()
#print(contatos_copia_1)
print(contatos_copia)

#Fromkeys - Usado para criar um dicionário com valores padrão
pessoa = dict.fromkeys(['nome', 'telefone']) #{'nome': None, 'telefone': None}
print(pessoa)
pessoa_exemplo = dict.fromkeys(['nome', 'telefone'], 'Vazio') #{'nome': 'Vazio', 'telefone': 'Vazio'}
print(pessoa_exemplo)

#Get - Uma forma de se acessar os dados do dicionário
print(contatos_copia.get('murilo@gmail.com', {}))
print(contatos_copia.get('claudia@gmail.com', {})) #Caso a chave não exista, ele irá retornar o segundo termo: {}

#Items - Usado principalmente quando for iterar dicionários
person = {
    'claudia@gmail.com': {'nome': 'Claudia', 'telefone': '1234-4567'}
}
print(person.items())

#Keys - Usado para saber quais são as chaves do dicionário
print(contatos_copia.keys())

#Pop - Usado para remover uma chave
print(person.pop('claudia@gmail.com'))
print(person.pop('luiza@gmail.com', {})) #Caso não exista essa chave ele retornará o valor padrão estabelecido: {}

#Popitem - Usado para remover items do dicionário. Mas não é informado o valor da chave
#Se não existir o que retirar da chave ele dará um 'keyError' como retorno
person = {
    'luiza@gmail.com': {'nome': 'Luiza', 'telefone': '0789-1234'}
}
print(person.popitem())
"""
print(person.popitem()) #keyError
"""

#Set default - Usado para criar valores padrão não informados
"""
CUIDADO ele não consegui mudar o dicionário interno somente o mais externo.
"""
person = {
    'luiza@gmail.com': {'nome': 'Luiza', 'telefone': '0789-9547'},
    'murilo@gmail.com': {'nome': 'Murilo', 'telefone': '5487-5218', 'idade': 20}
}
#person.setdefault('telefone', '****-****')
#person.setdefault('idade', 0)
#print(person)

"""
Abaixo está da forma correts para ele ver o dicionário seguinte.
"""
for email, info in person.items():
    info.setdefault('nome', 'Vazio')
    info.setdefault('telefone', '****-****')
    info.setdefault('idade', 0)

print(person)

#Update - Usado para atualizar um item no dicionário
person.update({'luiza@gmail.com': {'nome': 'Luiza', 'telefone': '0789-9547', 'idade': 24}})
print(person)

#Values - Usado para retornar os valores atribuidos as chaves
print(person.values())

#In - Usado para saber se a chave se encontra em determinado dicionário
print('luiza@gmail.com' in person) #True
print('idade' in person['murilo@gmail.com']) #True
print('cidade' in person['murilo@gmail.com']) #False

#Del - Usado para remover um valor ou uma chave inteira
person = {
    'luiza@gmail.com': {'nome': 'Luiza', 'telefone': '0789-9547', 'idade': 24},
    'murilo@gmail.com': {'nome': 'Murilo', 'telefone': '1981-8498', 'idade': 20},
    'claudia@gmail.com': {'nome': 'Clauida', 'telefone': '4519-7869', 'idade': 45}
}
del person['luiza@gmail.com']['idade'] #Deletará apenas a chave idade
del person['claudia@gmail.com'] #Deletará toda a chave
print(person)



