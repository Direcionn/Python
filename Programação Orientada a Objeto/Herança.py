#Sintaxe da herança simples
class A:
    pass

class B(A):
    pass

#Exemplo de utilidades
class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
        print(f'O veiculo de cor {cor}, com placa {placa}, tem {num_rodas} rodas.')
    
    def ligar_motor(self):
        print('Ligando o motor...')

class Carro(Veiculo):
    pass

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carga):
        #O 'super' chama a implementação da classe mãe
        super().__init__(cor, placa, num_rodas)
        self.carga = carga
    
    def mostrar_carga(self):
        print(f"{'Sim' if self.carga else 'Não'} tem carga no momento.")

carro = Carro('Preta', 'UFE-8475', 4)
caminhao = Caminhao('Branca', 'PFN-8438', 8, True)
caminhao.mostrar_carga()


#Sintaxe herança múltipla
class C:
    pass

class D:
    pass

class E(C, D):
    pass

#Exemplo de utilidade
class Animal:
    def __init__(self, num_patas, cor_pelo):
        self.num_patas = num_patas
        self.cor_pelo = cor_pelo
        print(f'O animal tem {num_patas} patas e sua pelagem tem cor {cor_pelo}')

class Mamifero(Animal):
    #O '**kw' denominado kwargs, serve para o interpretador do Python entender que se trata da mesma variavel em diferentes locais e não dar erro.
    def __init__(self, num_patas, cor_pelo, **kw):
        super().__init__(num_patas, cor_pelo, **kw)

class Ave(Animal):
    def __init__(self, num_patas, cor_pelo, cor_bico, **kw ):
        self.cor_bico = cor_bico
        super().__init__(num_patas, cor_pelo, **kw)
        print(f'Seu bico tem cor {cor_bico}')

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato1 = Gato(num_patas = 4, cor_pelo = 'Laranja')
#Por conta do kwargs os parametros tem que ser nomeados.
ornitorrinco1 = Ornitorrinco(num_patas = 4, cor_pelo = 'Vermelho', cor_bico = 'Laranja') 




