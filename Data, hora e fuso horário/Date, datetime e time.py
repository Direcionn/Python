#Datetime - Usado para lidar com datas e horas. Possui classe como date, time e timedata

#É necessário importar o modulo 'datetime'
import datetime

#Os argumentos são na ordem ano-mês-dia
#O metodo 'datetime' tem como ordem ano-mês-dia-hora-minutos-segundos

data = datetime.datetime.today()
print(f'A data de hoje é {data}')

#O metodo 'today' retorna a data atual.

data = datetime.date.today()
print(f'A data de hoje é {data}')

#O metodo 'time' tem como ordem hora-minutos-segundos
data = datetime.time(4, 21, 54)
print(f'A hora atual é {data}')



