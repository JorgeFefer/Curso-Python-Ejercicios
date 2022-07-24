from datetime import datetime
import string
import random
import csv

cantidad = 1
largo = 8
for x in range(cantidad):
  codigo=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(largo))

nombre=input("Ingrese el nombre: ")
direccion=input("Ingrese la direccion: ")
telefono=input("Ingrese el telefono: ")
fecha=datetime.today().strftime('%Y-%m-%d')
id=codigo

diccionario = {"nombre":nombre, "direccion": direccion, "telefono": telefono, "fecha": fecha, "id": id }

with open ("addresses.csv", "w") as csvarchivo:
    fieldnames = ["nombre", "direccion", "telefono", "fecha", "id"]
    writer = csv.DictWriter(csvarchivo, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(diccionario)

