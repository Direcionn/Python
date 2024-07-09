#If simples
saldo = 2000.0
#Sempre colocar o tipo de dados após a sua declaração
saque = float(input("Infome seu saque: "))

if saque<=saldo:
    print("Saque realizado.")
    saldo -=saque
    #Sempre transformar em string quando for para colocar em algum texto.
    str(saldo)
    print(f'Novo saldo de {saldo}')

if saque>=saldo:
    print("Saldo insuficiente.")
    str(saldo)
    print(f'Saldo atual é de {saldo}')

#If / else
if saque<=saldo:
    print('Saque realizado.')
else:
    print('Saldo insuficiente')
    str(saldo)
    print(f'Saldo atual é de {saldo}')

#If / elif / else
opcao = int(input('Informe uma das opções: [1]saldo, [2]saque\n'))

if opcao==1:
    str(saldo)
    print(f'Seu saldo é de {saldo}')
elif opcao==2 and saque<=saldo:
    str(saque)
    print(f'O valor sacado foi {saque}')
elif opcao==2 and saque>saldo:
    str(saque)
    #str(saldo)
    print(f'O saque de {saque}, não pode ser realizado, pois o saldo atual é de {saldo}')
else:
    print('Opção invalida')

#If aninhado (if dentro de if)
if opcao==1:
    str(saldo)
    print(f'Seu saldo é de {saldo}')
elif opcao==2:
    if saque<=saldo:
        str(saque)
        print(f'O valor sacado foi {saque}')
    else:
        str(saque)
        str(saldo)
        print(f'O saque de {saque}, não pode ser realizado, pois o saldo atual é de {saldo}')
else:
    print('Opção invalida')

#If ternário (Só utilizar em caso de duas opçoes ou 50/50)
status = "Sucesso" if saque<=saldo else "Falha"
print(f'{status} ao realizar o saque.')

