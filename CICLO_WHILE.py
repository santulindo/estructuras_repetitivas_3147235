#EJERCICIO 1
#imprimir la tabala de multiplicar 
# que un usuario ingrese 
# por teclado utilizando el ciclo
#  while

numero = int(input("Ingrese un numero: "))
i = 10
while i >= 1 :
    resultado = numero * i
    print(numero, "X" , i, "=",resultado ) 
    i = i -1 