#Usamos '_' no inicio da variavel para informar que aquela variavel é privada,
#pois todos os recursos em Python são públicos e foi adotada essa convenção do underline(_)
class Conta:
    def __init__(self, saldo = 0):
        #A variavel 'saldo' está privada pela convenção adotada
        self._saldo = saldo

    def Depositar(self, valor):
        self._saldo += valor
        print(f'Foi realizado a ação de depósito com o valor de {valor:.2f}')

    def Sacar(self, valor):
        self._saldo -= valor
        print(f'Foi realizado a ação de saque com o valor de {valor:.2f}')

    #Método utilizado para exibir uma variável privada
    def Mostar_saldo(self):
        print(f'O saldo atual é de R${self._saldo:.2f}')

conta = Conta(100)
conta.Depositar(100.65)
conta.Sacar(50.24)
conta.Mostar_saldo()

#Propriedades
class Foo:
    def __init__(self, x=None):
        self._x = x

    #Usado o 'property' para retornar o atributo sem ser necessario fazer outra operação
    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)

"""
Exemplo sem o property
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return 2022 - self._ano_nascimento

pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
"""

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento

    #O 'get' pode ser uma segunda opção do 'property', mas não é muito utilizado em Python
    def get_nome(self):
        return self.nome

    def get_idade(self):
        return 2022 - self._ano_nascimento

pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")


