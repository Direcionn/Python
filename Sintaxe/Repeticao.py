#For
texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letras in texto:
    #O .upper() transforma letra minuscula em maiscula
    if letras.upper() in VOGAIS:
        print(letras, end=' ')

#Realiza uma quebra de linha
print()

#For com range
for numero in range(0, 51, 5): #range(Da onde irá começar(opcional), Onde irá terminar(obrigatorio), De quanto em quanto irá pular(opcional))
    print(numero, end=' ')

