#Variáveis de classe e variáveis de instância
class Estudante:
    #Por se tratar de uma variável de classe sempre que modifica-la, todos irão sofrer a mudança.
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        #'Matricula' é uma variável de instância, então se eu modifila-la em um objeto somente ele sofrerá a mudança.
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

#Nesse exemplo irá mudar a variável escola de toda a classe e subsequentemente seus objetos tambem.
#Se fosse 'aluno_1.escola = "Python" somente ele iria sofrer a alteração.
Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

#Métodos de classe e métodos estáticos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #'@classmethod' é usado para criar um método de classe.
    @classmethod
    #Como primeiro argumento tem como convenção a utilização da palavra 'cls', que se referencia diretamente a classe.
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        #Por o 'cls' estar referenciando a classe 'Pessoa' pode se colocar ele ao inves de 'Pessoa' para a declaração.
        return cls(nome, idade)

    #'@staticmethod' é usado para criar um método estático.
    @staticmethod
    #Ele não precisa de um primeiro argumento especial, pode ser desenvolvido até sem argumento.
    def e_maior_idade(idade):
        if idade >= 18:
            print(f"A pessoa com {idade} anos é maior de idade.")
        else:
            print(f"A pessoa com {idade} anos é menor de idade.")

#Por se tratar de um método de classe não é necessário colocar 'Pessoa()', pois o método já faz referencia a classe.
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

Pessoa.e_maior_idade(18)
Pessoa.e_maior_idade(8)

#Classes abstratas - '@abstractmethod'
from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)


