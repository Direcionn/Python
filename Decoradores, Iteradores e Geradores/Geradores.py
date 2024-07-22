#Gerador - Usado para códigos mais simples e seu retorno de valores utiliza a palavra 'yield'
def Meu_Gerador(numeros: list[int]):
    for numero in numeros:
        yield numero, numero * 2

for numeros, numero in Meu_Gerador([4, 8, 42]):
    print(f'O número {numeros} tem como dobro o valor {numero}.')        


