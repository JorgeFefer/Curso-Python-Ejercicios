#from asyncore import write
#import csv

from datetime import datetime
import string
import random
import csv

cantidad = 1
largo = 8
for x in range(cantidad):
  codigo=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(largo))

nombre = (input("ingrese un nombre para registrar en su agenda " ))

direccion = (input ("ingrese la direccion "))

telefono = (input("ingrese el numero de telefono "))

id = codigo 

diccionario = {'nombre' :'nombre', 'direccion' : 'deireccion', 'telefono' : 'telefono', 'id' : 'id'}


with  open ("adress.csv","w") as csvarchivo:
    fieldnames = ['nombre', 'direccion', 'telefono', 'id']
    writer = csv.DictWriter(csvarchivo, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow (diccionario)

print(datetime.today())