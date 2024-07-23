#Pytz - Usado para formatar datas e horas no horário UTC
import datetime
import pytz

#O argumento usado dentro do timezone é padronizado pelo proprio 'pytz', então não tem como mudar a grafia.
data_LA = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
data_Paris = datetime.datetime.now(pytz.timezone('Europe/Paris'))
data_London = datetime.datetime.now(pytz.timezone('Europe/London'))
data_Tokyo = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

print(data_LA)
print(data_Paris)
print(data_London)
print(data_Tokyo)



