"""
O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação Orientada a Objetos (POO). 
A classe deve conter um método para realizar a operação de soma entre dois números inteiros, 
encapsulando assim a lógica matemática da adição.
"""
class Calculadora:
    def Somar(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        return num_1 + num_2
    
    def Subtrair(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        return num_1 - num_2
    
    def Multiplicar(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        return num_1 * num_2
    
    def Dividir(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        return num_1 / num_2

menu = """
[1]Somar
[2]Subtrair
[3]Multiplicar
[4]Dividir
[0]Sair
"""
calculo = Calculadora()

while True:
    print(menu)
    opcao = input("Digite qual é a operação: ")

    if opcao == '1':
        num_1 = int(input('Digite um número: '))
        num_2 = int(input('Digite um número: '))
        resultado = calculo.Somar(num_1, num_2)
        print(f'O resultado da soma entre {num_1} e {num_2} é igual a {resultado}')
    
    elif opcao == '2':
        num_1 = int(input('Digite um número: '))
        num_2 = int(input('Digite um número: '))
        resultado = calculo.Subtrair(num_1, num_2)
        print(f'O resultado da subtração entre {num_1} e {num_2} é igual a {resultado}')

    elif opcao == '3':
        num_1 = int(input('Digite um número: '))
        num_2 = int(input('Digite um número: '))
        resultado = calculo.Multiplicar(num_1, num_2)
        print(f'O resultado da multiplicação entre {num_1} e {num_2} é igual a {resultado}')

    elif opcao == '4':
        num_1 = int(input('Digite um número: '))
        num_2 = int(input('Digite um número: '))
        resultado = calculo.Dividir(num_1, num_2)
        print(f'O resultado da divisão entre {num_1} e {num_2} é igual a {resultado:.2f}')

    else:
        print('Obrigado pelo uso do programa.')
        break




