#Strfttime - Usado para formatar datas
import datetime

d = datetime.datetime.now()
print(d)
print(d.strftime('%d/%m/%Y  %H:%M'))

#Strptime - Usado para transformar strings em data e hora
data_string = '20/07/2024   18:41'
data = datetime.datetime.strptime(data_string, '%d/%m/%Y    %H:%M')
print(data)




