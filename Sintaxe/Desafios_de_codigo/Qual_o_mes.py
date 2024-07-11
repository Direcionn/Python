"""
Leia um valor inteiro entre 1 e 12, inclusive. 
Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, 
em inglês, com a primeira letra maiúscula.

Auxilio do ChatGPT, pois esse curso foi descontinuado, provavelmente por inconsistencias dos desafios propostos.
Não havia visto sobre dicionarios ainda.
"""
mes = int(input("Digite o número do mês: "))

month_dic = {
    1: 'January', 2: 'February', 3: 'March',
    4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'
}

if 1 <= mes <= 12:
    print(month_dic[mes])
else:
    print("Número invalido.")

