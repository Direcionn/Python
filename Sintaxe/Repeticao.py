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

#While
opcao = -1
while opcao!=0:
    opcao = int(input('[1]Sacar\n[2]Extrato\n[0]Sair\n: '))

    if opcao==1:
        print('Sacando...')
    elif opcao==2:
        print('Exibindo o extrato...')

else: 
    print('Saindo do sistema')

