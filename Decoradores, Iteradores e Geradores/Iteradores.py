#Iterador - Usado para percorrer todos os valores de uma sequência(listas, tabelas etc),
#é necessário usar dois metodos especiais '__iter__()' e o '__next__()'
class Meu_Iterador:
    def __init__(self, numeros: list [int]):
        self.numeros = numeros
        self.contador = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero_original = self.numeros[self.contador]
            self.contador += 1
            return numero_original, numero_original * 2
        except IndexError:
            raise StopIteration
        
for numero_atual, numero_modificado in Meu_Iterador(numeros = [4, 8, 54]):
    print(f'O valor {numero_atual} multiplicado por 2 é {numero_modificado}.')



