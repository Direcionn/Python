#Funçao - Usado para tornar o código mais legível e poder ser reaproveitado
def exibir_mensagem():
    print('Hello World!')
def exibir_mensagem_2(nome):
    print(f'Seja bem vindo {nome}')
def exibir_mensagem_3(nome = 'Anonimo'):
    print(f'Seja bem vindo {nome}')

exibir_mensagem()
exibir_mensagem_2(nome = 'Murilo') #Caso queira colocar a variavel e seu valor atribuido
exibir_mensagem_3()
exibir_mensagem_3('Chappie') #Caso queira colocar apenas o valor atribuido

#Retorno de valor - Em Python utiliza-se a palavra 'return' e a função pode retornar mais de um valor
def calcular_numeros(numeros):
    print(sum(numeros)) #A palavra 'sum' é uma função do Python para somar elementos de uma lista ou tupla
def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

calcular_numeros([10, 20, 34])
print(retornar_antecessor_e_sucessor(10))

#Argumentos nomeados - Usado a forma de chave = valor
def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234')
"""
Outras formas de se nomear:
salvar_carro(marca = 'Fiat', modelo = 'Palio', ano = 1999, placa = 'ABC-1234')
salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1234')}
Os ** informa que o que vir a seguir será um dicionário.
"""

#Args e kwargs - Usados para se referirem a tuplas e dicionários, respectivamente
"""
Tudo que vir a seguir da data por extenso e tiver separado por vírgula, o código considerará como tupla,
o que faz com que estejam tudo dentro da variável '*args'.
Após ele perceber que o valor seguinte é uma chave=valor, ele irá ser considerado como dicionário,
o que acarreta em entrar na variável '**kwargs'.
"""
def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('\nSexta-feira, 26 de Agosto de 2023','Zen of Python', 'Beautiful is better than ugly', autor = 'Tim Peters', ano = 1999)

#Keyword only - Usando um '*' no começo da frase, você obriga a chamada da função ser em forma de chave=valor.
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro(modelo = 'Palio', ano = 1999, placa = 'ABC-1234', 
            marca = 'Fiat', motor = '1.0', combustivel = 'Gasolina')

#Objetos de primeira classe - Usado para colocar função dentro de outra ou em variáveis
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    if funcao == somar:
        print(f'O resultado de {a} + {b} = {resultado}')
    else:
        print(f'O resultado de {a} - {b} = {resultado}')

exibir_resultado(10, 10, subtrair)

#Escopo local e escopo global - Usar a palavra 'global' para informar ao interpretador da intenção
#NÂO é uma boa prática e deve ser evitada.
"""
Exemplode variável global
salario = 2000

def salario_bonus(bonus):
    #salario = int(input("Digite seu salário: "))
    #cheque = int(input('Digite seu bônus: '))
    global salario
    salario += bonus
    #print(f'Seu salário com o bônus é de {salario}')
    return salario

salario_bonus(500)
print(f'Seu salário com o bônus é de {salario}')
"""
def salario_bonus():
    salario = int(input("Digite seu salário: "))
    cheque = int(input('Digite seu bônus: '))
    salario += cheque
    return salario

salario_com_bonus = salario_bonus()
print(f'Seu salário com o bônus é de {salario_com_bonus}')

