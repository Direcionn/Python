"""
Neste desafio, deve-se escrever uma solução que receba um número inteiro como entrada e 
determine se ele é par ou ímpar. Dessa forma, 
a solução deve retornar uma string indicando Par se o número for par e 
Ímpar se o número for ímpar.
"""

# Solicita ao usuário um número inteiro
numero = int(input('Digite um número: '))

# TODO: Verifique se o número é par ou ímpar e imprima o resultado:
if numero%2 ==0:
    print("O número informado é par.")
else:
    print("O número informado é ímpar.")

