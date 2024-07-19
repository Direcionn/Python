"""
Problema:
João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Criar um programa onde João informe:
cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr.
"""
class Bicicleta:
    #O init serve como um inicializador
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        print(f'A bicicleta de cor {cor} de modelo {modelo} do ano de {ano}, custa R${valor},00.\n')
    
    #A palavra 'self' é obrigatoria em todos os metodos/funções em Python
    def buzinar(self):
        print('Plim plim ...')
    
    def parar(self):
        print('Freiando a bicicleta')
        print("Bicicleta parada")

    def correr(self):
        print("Pedalando com força!")
    
    #Retorna os valores atribuidos as chaves e não precisa fazer manualmente todas as vezes que mudar.
    def __str__(self):
       return f'{self.__class__.__name__}: {", ".join([f"{chave}= {valor}" for chave, valor in self.__dict__.items()])}'


#b1 = Bicicleta('Vermelha', 'BMX', 2022, 640)
cor = input('Digite a cor da bicicleta: ')
modelo = input('Digite o modelo da bicicleta: ')
ano = int(input('Digite o ano da bicicleta: '))
valor = int(input('Digite o valor da bicicleta: '))
b1 = Bicicleta(cor, modelo, ano, valor)
print(b1)
b1.buzinar()
b1.correr()
b1.parar()

#b2 = Bicicleta('Verde', 'Caloi', 2014, 54)
#print(b2)



