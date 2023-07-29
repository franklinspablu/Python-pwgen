#Programa generador de contraseñas @frankpablu

import random
from typing import Generator 

min= "abcdefghijklmnñopqrsuvwxyz"
may= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
num= "0123456789"
sim= "[]{}()*;/,._-"

res = min + may + num + sim
lon = 16
contraseña = "".join(random.sample(res,lon))
print (contraseña)







