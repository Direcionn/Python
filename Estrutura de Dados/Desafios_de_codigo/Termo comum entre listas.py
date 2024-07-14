"""
Desenvolva uma função que receba duas listas de números inteiros separados por espaço 
e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.
"""
def elementos_comuns(lista1, lista2):
    return list(set(lista1).intersection(set(lista2)))

lista1 = input("Digite uma lista de números com espaços entre eles, após digitar aperte enter: ").split()
lista2 = input("Digite outra lista de números com espaços entre eles: ").split()

#Estrutura condicional para saber se todos os elementos das listas são inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida de dados, somente números inteiros.")


