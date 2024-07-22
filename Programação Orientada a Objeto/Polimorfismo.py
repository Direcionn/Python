#Por vezes o que é herdado da classe mãe não se encaixa com o que é proprosto na classe filha.
#E o polimorfismo permite que em diferentes classes, os mesmos métodos atuem de forma diferentes.
class Passaro:
    def Voar(self):
        pass

class Pardal(Passaro):
    def Voar(self):
        print('Pardal consegue voar.')

class Avestruz(Passaro):
    def Voar(self):
        print('Avestruz não consegue voar.')

def plano_de_voo(passaro):
    passaro.Voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())


