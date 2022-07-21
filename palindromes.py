clave_salida = "bye"
cant_palabras = 0
cant_palindromos = 0
cant_nopalindromos = 0

palabra = input ("Ingrese una palabra: ")

while palabra != clave_salida:
        
    
    palabra_1 = list(palabra)
    palabra_2 = list (reversed (palabra_1))
    palabra_3 = "".join(palabra_2)
    
    if (palabra==palabra_3):
        print ('La palabra ingresada en palindromo')
        cant_palabras+=1
        cant_palindromos+=1
    else:
        print ('La palabra ingresada no es un palindromo')
        cant_palabras+=1
        cant_nopalindromos+=1
        
    palabra = input ('Ingrese una palabra: ')
        
print(f"Usted ingreso un total de {cant_palabras} palabras de las cuales {cant_palindromos} fueron palindromos y {cant_nopalindromos} no fueron palindromos")      
        
    
        
        
    



    
        
        
        
         
         
        
    
    
   