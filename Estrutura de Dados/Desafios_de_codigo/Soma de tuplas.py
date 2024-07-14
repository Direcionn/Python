"""
Desenvolva uma função em Python que recebe uma tupla de números inteiros e retorna a soma de todos os elementos dessa tupla. 
A função deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que todos os elementos sejam números inteiros. 
O objetivo é praticar a manipulação de tuplas e a utilização de funções em Python.
"""
def somar_tupla(*tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input('Digite números separados por espaços: ')
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))
    
    resultado = somar_tupla(*elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")

