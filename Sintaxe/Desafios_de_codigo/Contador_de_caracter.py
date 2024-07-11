"""
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
Conferir se um texto vai caber em um tuíte é sua tarefa.
"""
texto = input("Digite seu tweet: ")

if len(texto) <= 140:
  print("Sua mensagem foi aprovado pelo contador.")
else:
  print("Diminua o tamanho da mensagem.")

