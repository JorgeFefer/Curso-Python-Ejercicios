word1= str(input("Ingrese una oracion: "))
palabra_de_salida = "the end"
palabra_de_salida1 = "show time"
palabra_de_salida2 = "abra cadabra"

#f = open ("palabras.txt",'a')
#f.write(palabras+'\n')

while word1 == palabra_de_salida or word1 == palabra_de_salida1 or word1 == palabra_de_salida2:
    print("Esta oracion no esta permitida, vuelva a intentarlo, en otro momento. Gracias: ")
else:
    print("La palabra: " , word1, "tiene", len(word1), "letras")
    word2= str(input("Ingrese otra oracion: "))
    print("La palabra: " , word2, "tiene", len(word2), "letras")
    total_word = print(" Hay ", len(word1.split()) + len(word2.split()), "palabras")
    print("Con ", len(word1) , "y", len(word2), "letras cada una")
#file.close()
