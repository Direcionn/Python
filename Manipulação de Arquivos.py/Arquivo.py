#Abrindo e fechando arquivos - Usa-se open() e close()
file = open('C:\DIO\Python\Manipulação de Arquivos.py\Texto exemplo.txt', 'r')
print(file.read())
file.close()


#Leitura de arquivos - Usa-se 'read()', 'readline()' e 'readlines()'.
"""
read(): Lê todo o texto do arquivo.
readline(): Retorna apenas uma linha do texto.
readlines(): Retorna todas as linhas do arquivo em formato de uma lista.
Para se trabalhar da melhor forma com readlines() é preferivel usar iteradores.
Ex.
for linha in file.readlines():
    print(linha)
"""

#Escrita de arquivo - Usa-se 'write()' e 'writelines()'. Lembre-se de abrir o arquivo no modo correto.
file = open('C:\DIO\Python\Manipulação de Arquivos.py\Texto exemplo.txt', 'w')
file.write("""
Olá meu nome é Murilo Vieira, tenho 20 anos
e no momento estou estudando Python para uma carreira na área de segurança da informação.
Atualmente estou desempregado, mas estou correndo atrás de uma oportunidade de estágio.
""")
file.close()

#Gerenciamento de arquivos e diretórios
"""
Pode-se criar, renomear e excluir arquivos e diretórios usando os módulos:
    - os
    - shutil
Ex.
import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
"""

#Tratamento de Exceção - O Python permite lidar com erros comuns
"""
- FileNotFoundError: Lançada quando o arquivo que está sendo aberto não é encontrado no diretorio especifico.
- PermissionError: lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas
para leitura ou gravação.
- IOError: Lançada quando ocorre um erro geral de E/S ao trabalhar com o arquivo, como problemas de permissão,
falta de espaço em disco, entre outros.
- UnicodeDecodeError: Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto
usando uma codificação inadequada.
- UnicodeEncodeError: Lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificação
ao gravar em um arquivo de texto.
- IsADirectoryError: Lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo texto. 
"""
try:
    file = open('inexistente.txt', 'r')
except FileNotFoundError:
    print('Arquivo não encontrado.')

#Boas práticas em manipulação de arquivos
"""
Bloco with: Permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente,
mesmo em caso de exceções.
Ex.
with open('arquivo.txt', 'r') as file:
    #Lógica operacional do método
"""
"""
Verificar se o arquivo foi aberto antes de manusea-lo.
Ex.
try:
    with open('arquivo.txt') as file:
        #Lógica do método
except IOError:
    print('Não foi possível abrir o arquivo.')
"""

#Trabalhando com arquivos CSV
"Escrita em arquivo .CSV"
import csv

try:
    with open('C:\DIO\Python\Manipulação de Arquivos.py\example.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['nome', 'idade'])
        writer.writerow(['Ana', 30])
        writer.writerow(['João', 25])
        print(file)
except FileNotFoundError:
    print('Arquivo não encontrado.')

"Leitura de arquivo .CSV"
try:
    with open('C:\DIO\Python\Manipulação de Arquivos.py\example.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print('Arquivo não encontrado.')






