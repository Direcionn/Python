"""
O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. 
Vamos iterar através de cada caractere na string string. Para cada caractere, 
verifique se ele já está presente no dicionário contador. 
Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. 
Neste dicionário, as chaves são os caracteres presentes na string 
e os valores correspondem à contagem de vezes que cada caractere aparece.
"""
def contar_caracteres(string):
    contador = {}  # Dicionário para armazenar as contagens de caracteres

    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1  # Incrementa a contagem se o caractere já estiver no dicionário
        else:
            contador[caractere] = 1  # Adiciona o caractere ao dicionário com valor inicial 1

    return contador

# Exemplo de uso
string = input("Digite um texto: ")
resultado = contar_caracteres(string)
print(f"A contagem de caracteres no texto é: {resultado}")


