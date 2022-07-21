import random
import string

mayusculas= input ("Desea incluir mayusculas: (si/no): ")   
minusculas= input ("Desea incluir minusculas? (si/no): ")
numeros= input ("Desea incluir numeros? (si/no): ")
caracteres= input ("Desea incluir caracteres? (si/no): ")
longitud=abs(int(input ("Ingrese la longitud deseada: ")))
cantidad=1
arrastre=""

if (mayusculas=="no" and minusculas=="no" and numeros=="no" and caracteres=="no"):
    largo = 16
    for x in range(cantidad):
        print (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(largo)))
            
if (mayusculas=="si"):
    arrastre= string.ascii_uppercase
if (minusculas=="si"):        
    arrastre=arrastre + string.ascii_lowercase
if (numeros=="si"):
    arrastre=arrastre + string.digits
if (caracteres=="si"):
    arrastre=arrastre+string.punctuation 
    
for x in range(cantidad): 
    print (''.join(random.choice(arrastre) for _ in range(longitud)))
  
  
  
  
