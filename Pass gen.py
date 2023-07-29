import random
from typing import Generator 
long = 0
min= "abcdefghijklmnñopqrsuvwxyz"
may= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
num= "0123456789"
sim= "[]{}()*;/,._-"

res = min + may + num + sim
print("How long do you want?")
long = input("We recommend more than 16 characters")

contraseña = "".join(random.sample(res,long))
print (contraseña)







