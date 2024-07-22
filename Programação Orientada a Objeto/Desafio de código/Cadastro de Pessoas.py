"""
Neste desafio, temos a classe Pessoa com seus atributos que armazenam o nome e a idade de uma pessoa. 
Implemente um método para retornar uma representação formatada dos dados da pessoa, crie uma instância da pessoa e, 
por fim, chame o método para retornar as informações formatadas e imprimir o resultado. 
O objetivo é utilizarmos formas para criar e manipular objetos com POO, 
usando atributos e métodos para encapsular dados e comportamentos.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade
    
    #Outra forma de se fazer
    #def get_nome(self):
        #return self.nome

    #def get_idade(self):
        #return self.idade

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

pessoa = Pessoa(nome, idade)
print(f'Nome: {pessoa.nome}\tIdade: {pessoa.idade}')
#Outra forma de se chamar.
#print(f"Nome: {pessoa.get_nome()}\tIdade: {pessoa.get_idade()}")
