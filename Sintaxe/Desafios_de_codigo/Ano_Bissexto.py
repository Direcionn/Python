"""
Escrever uma solução que informe se um determinado ano é bissexto. 
Um ano é considerado bissexto se ele for divisível por 4. 
No entanto, anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400. 
Esta regra é usada para corrigir o calendário, de modo que ele fique em conformidade com o ano solar.
"""
ano = int(input('Indique um ano papa ver se ele é bissexto: '))

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    str(ano)
    print(f"O ano {ano} é bissexto.")
else:
    str(ano)
    print(f"O ano {ano} não é bissexto.")

