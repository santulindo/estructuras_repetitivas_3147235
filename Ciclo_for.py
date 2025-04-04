#CICLO FOR 
#Especial parra recorrer 
#estructuras de datos 
#Todo lo que esta entre 
# []se denomina una lista 

# Funcion range (python)
# : crea un lista de numeros 
# en  el rango deifinido 
# por el ususario

numero = int(input("Ingrese un numero: "))

for i in range (1, 11):
    resultado = numero * i
    print(numero, "X" , i, "=",resultado ) 