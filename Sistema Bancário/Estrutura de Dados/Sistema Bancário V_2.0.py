import sys

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor < 0:
        print('Valor negativo informado. Por motivos de segurança o programa foi encerrado.')
        sys.exit()

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f'O valor informado (R${valor}) excede o saldo atual.')
    elif excedeu_limite:
        print(f'O valor informado (R${valor}) excede o limite atual R${limite}.')
    elif excedeu_saques:
        print('O limite de saque foi atingido. Não será possível realizar saque até amanhã.')
    elif valor > 0:
        saldo -= valor
        print(f'Saque de {valor} realizado com sucesso')
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    return saldo, extrato, numero_saques

def depositar(*, saldo, valor, extrato):
    if valor < 0:
        print('Valor negativo informado. Por motivos de segurança o programa foi encerrado.')
        sys.exit()
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print('Depósito realizado com sucesso.')
        
    return saldo, extrato

def mostrar_extrato(*, saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    menu = """
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [0] Sair
    """

    while True:
        print(menu)
        opcao = input('Digite o número da operação desejada: ')

        if opcao == '1':
            valor = float(input('Digite o valor desejado de saque: '))
            saldo, extrato, numero_saques = sacar(saldo=saldo,
                                                  valor=valor,
                                                  extrato=extrato,
                                                  limite=limite,
                                                  numero_saques=numero_saques,
                                                  limite_saques=LIMITE_SAQUES)
        elif opcao == '2':
            valor = float(input('Informe o valor de depósito: '))
            saldo, extrato = depositar(saldo=saldo,
                                       valor=valor,
                                       extrato=extrato)
        elif opcao == '3':
            mostrar_extrato(saldo=saldo, extrato=extrato)
        elif opcao == '0':
            print('Obrigado pelo uso. Volte sempre.')
            break
        else:
            print("Operação inválida, por segurança o sistema será fechado.")
            break

main()
