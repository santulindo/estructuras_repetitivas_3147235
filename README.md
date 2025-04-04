# Estructuras repetitivas 3147235
Proyecto para trabjar el for y while en python
## Conceptos Clave para en trabajar en ciclos 
* **Breakóint(punto de interrupcion)**:hermienta
 para ejeuctar codigo, un instrucion a la vez (depuracio - debugger)
 Permite ver el valor de las variabeles definidas en un progrma a traves dde la ejucucion del codigo permitiendo observan el comportamineto del programa/codigo  a traves del tiempo
* **Variable contadora(contador)**: es una variable a la cual podemos aumentar (disminuir)su valor en un determinada cantidas constante de 1 en 1 de 2 en 2 etc... 
- una variante contadora se debe inicializar 
 **antes de la estructura repetitiva**con el v valor inicial (0)
- Una varibles contadora, por lo general      se   nombre con las letras i,j 
- un avaribale contadora debe participar en un **condicional del ciclo**
-toda variable contadora debe tener lo que se denomina **Una instruccion de incremento** para aumentar su valor 
- En un ciclo while, la instruccion de incremeno se pode  **al final del bloque del ciclo**

* **Iteraccion** : Es un recorrido en la ejucucion de un ciclo 
## Ciclo while 
Estructura que permite ejecutar un bloque de codigo un numero determinado de veces.

EL bloque de codigo dentro del ciclo while se repetira o se ejecutara sucesivamente **mientras la condiconal sea evaluada como VERDAD.** 
### Sintaxis en python:
```
While condicional:
      instrucion1 
      instrucion2
      instrucion3
      ....
      instrucion n 
```
## Ciclo for
Se utiliza (python) para recorrer conjuntos de datos (estructueas de datos-coleccion de datos)
*el ciclo recorrera cada dato en la estructura **dede el primero hasta el ultimo**.
*el elemento recorrido se asigna a la varible en el ciclo 
### Sintaxis For 
```
for <variable>in <conjunto datos>:
       instrucion1 
       instrucion2
       instrucion3
      ....
       instrucion n 
```