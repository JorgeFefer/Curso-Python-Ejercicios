def fibonacci(numero):
    a=1
    b=1
    if numero==1:
        print('1')
    elif numero==2:
        print('1')
        print('1')
    else:
        print(a)
        print(b)
        for i in range(0,numero-2):
            total = a + b
            b=a
            a= total
            print(total)
       
numero = int (input("Ingrese un entero mayor a cero: "))
while numero < 1:
    print ("El numero ingresado no es un entero positivo")
    numero = int (input("Ingrese un entero mayor a cero: "))
    
fibonacci(numero)
    
    
    



               