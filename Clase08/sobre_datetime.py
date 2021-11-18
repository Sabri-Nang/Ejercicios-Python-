# -*- coding: utf-8 -*-
"""
Created on Sun May  9 01:31:54 2021

@author: Sabri
"""

import datetime

fecha_hora = datetime.datetime.now()
print(fecha_hora)

#obtener fecha actual
fecha = datetime.date.today()
print(fecha)

#Dentro del módulo datetime
print(dir(datetime))

#representar una fecha datetime.date(año, mes, dia)
d = datetime.date(2019, 4, 13)
print(d)

from datetime import date

d = date(2019, 4, 13)
print(d)

#timestamp toma como medida de tiempo lo segundos 
#transcurridos desde el 1 de enero de 1970 a las 0 horas UTC
timestamp = date.fromtimestamp(1326244364)
timestamp = date.fromtimestamp(0)
print('Fecha=', timestamp)


#%% Obtener año, mes y dia

from datetime import date

hoy = date.today()
print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual', hoy.day)
print('Día de la semana:', hoy.weekday())

#%% Representar la hora con un objeto time

from datetime import time

a = time() #time(hour = 0, minute = 0, second = 0)
print('a =', a)

b = time(11, 34, 56)
print('b =', b)

c = time(hour = 11, minute = 34, second = 56)
print('c =', c)

d = time(2, 34, 56, 1) #ultimo lugar, microsegundos
print('d = ', d)

#%% Obtener horas, minutos, segundos y microsegundos

a = time(11, 34, 56)

print('hour =', a.hour)
print('minute = ', a.minute)
print('second = ', a.second)
print('micosecond = ', a.microsecond)

#%% Clase datetime.datetime

from datetime import datetime

a = datetime(2020, 4, 21)
print(a)

#datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2021, 4, 21, 6, 53, 31, 342260)
print(b)

#Obtener timestamp. Los timestamp son enteros y no tienen en 
#cuenta la decima de segundos
print('timestamp = ', a.timestamp())

#%%Clase timedelta. Representa una duración

from datetime import datetime, date

t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)
t3 = t1 - t2
print(t3)

t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print(t6)

print('Tipo de t3 = ', type(t3))
print('tipo de t6 = ', type(t6))

#diferencia entre objetos timedelta es tambien timedelta
from datetime import timedelta

t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

#%%Imprimir objetos timedelta negativos

from datetime import timedelta

t1 = timedelta(seconds = 21)
t2 = timedelta(seconds = 55)
t3 = t1 - t2

print(t3)
print(abs(t3))

#%%Se puede obtener el tiempo medido en segundos usando el metodo
#total_seconds

from datetime import timedelta

t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundo totales =', t.total_seconds())

#%%Formato para fecha y horas
#Metodos strftime() y strptime()

#strftime() crea una cadena con formato a partir
#de clases date, datetime y time

from datetime import datetime

now = datetime.now()

t = now.strftime('%H:%M:%S')
print('hora: ', t)

s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
print('s1:', s1)

s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
print('s2: ', s2)

#El metodos strptime() crea un objeto datetime a partir 
#de una cadena

from datetime import datetime

cadena_con_fecha = '21 September, 2021'
print('date_string =', cadena_con_fecha)

date_object = datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('date_object = ', date_object)

#el metodo strptime() toma dos argumentos:
#una cadena q representa la fecha y hora 
#un codigo de formato correspondiente al primer argumento
#los codigos %d, %B, %Y significan day, month (full name) y 
#year respectivamente