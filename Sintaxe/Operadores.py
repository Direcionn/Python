#Operadores Lógicos
saldo = 1000
saque = 100
print(saque>=saldo and saque<=saldo)  #False

print(saldo>=saque or saque<=saldo)  #True

print(not saque>saldo)  #True

#Operadores de Identidade
curso ="Curso de Python"
nome_curso = curso
print(curso is nome_curso)  #True

print(curso is not nome_curso)  #False

#Operadores de Associação
curso = "Curso de Python"
fruta= ["Laranja", "Uva", "Banana"]
print("Python" in curso)    #True

print("Maça" not in fruta)  #True

