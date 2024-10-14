import math

# El bucler While

# el bucle While es una bucle indeterminado, es decir, no sabemos cunatas veces ejecutara el codigo que tiene en su interior.

# La sintaxis del while es la siguiente:
"""
i=1
while i<=10:
    print("Ejecucucion" + str(i))
    i+=1

print("Fin de la ejecucion")
"""

# A la hora de realizar tareas es necesario dependiendo de determinadas taeas de esta funciononalidad del bucle infinito.

#en este ejmplo haramoes un bucle infinito, en el que hasta que el usuario ingrese bien su edad el bucle se seguira ejecutando.

"""
edad=int(input("Ingrese su edad, por favor: "))

while edad<0 or edad>100:
    print("Ingrese una edad valida")
    edad=int(input("Ingrese su edad, por favor: "))
    
print("Graciasp or colaborar")

print("La edad del aspirante es: " + str(edad))
"""


# pero en ocaciones no se requiere o no es funcional que un bucle este repitiendose infinitamente.

# crearemos un programa que averigue la raiz cuadrada de un numero (la raiz cuadrada de un numero para poder hayar e l numero debe ser positivo)

print("Programa de calculo de raiz cuadrada")

numero = int(input("Ingrese un numero: "))

intentos=0

while numero<0:
    print("No se puede hayar la raiz cuadrada de un numeor negativo.")

    if intentos==2:
        print("Has realizado demasiados intentos.")
        #break se encarga de detener el bucle
        break

    numero = int(input("Ingrese un numero valido, por favor: "))

    if numero<0:
        intentos+=1

if intentos<2:
    #estamos haciendo el uso de una termino nuevo, en esete caso es una clase llamada math

    #para poder usar math debemos importarlo, para ello debemos escribimos al inicio del codigo import math
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es: " + str(solucion))