#Timedelta - Usado para manipular datas e horas
import datetime

d = datetime.datetime(2023, 7, 12, 13, 45)
print(d) # 2023-07-12   13:45:00

#Irá acrescentar mais uma semana a data informada.
d = d + datetime.timedelta(weeks = 1)
print(d) # 2023-07-19   13:45:00



