# veremos las instrucciones continues , pass y else: estas sintrucciones se pueden usar tanto en el bucle for como en el while.

# 1. continue:  Se encarga de saltar a la siguiente interaccion de bucle, hace que la vuelta de bucle en la que se encutre sea cortada y salta a la iteracion del bucle inmediatamnte, ejempli ,si estamos en la buelta 5 de bucle la lectura del codigo se encuentra con el cuntinue corta la iteracion del bucle y nos dirige a la iteracion 6.

"""
for letra in "python":

    if letra == "h":
        continue
    #en este caso al la lectura del codigo se encuentra con el continue, no ejecuta el print que sigue sino que pasa directamtne a la siguiente iteracion.

    print("viendo la letra: " + letra)

"""
    #ahora haremos un codigo que nos indique la cantidad de caracteres que tiene un texto por lo que no queremos que nos cuente el espacio quesepara las palabras (el espacio en blanco se le considera caracter).

"""
nombre = "pildoras informaticas"

contador = 0
for i in nombre:

    if i==" ":
        continue
    contador+=1


print(len(nombre))
"""

# 2. pass: Pass se encarga de devolver null en cuanto es leida en el interior de un bucle, el bucle devuelve null es como si no ejecutara el bucle.

    #la funcion pass no es muy utilizada en python ya que su fucnion es hacer que el bucle no se ejecute, pero es muy util cuando se quiere crear un bucle pero no se quiere hacer nada dentro del bucle.

    #este codigo con el while True nos permite que el bucle se ejecute infinitamente hasta que el usuario preciona por ejemplo ctrl + c.
"""
while True:
    pass
"""

    #otro uso es cuando queremos crear una clase lo mas pequeña posible, que en un futuro completaremos.
"""
class MiClase:
    pass # clase para implementar mas tarde
"""

# 3. else: else funciona similar a como lo hace en un condicional, aunque se pueden conseguir los mismos resultados sin esta intruccion cuando se trata de bucles.

email = input("ingrese su email: ")

for i in email:

    if i == "@":
        arroba = True
        break

else: # el else se suele interpretar que si no se cumple la parte superir del ciclo ejecutes el else pero en  realidad no funciona de esta forma. La intruccion else se va a ejecutrarse simpre y cuando el bucle este vacio (osea que el bucle no devulva nada) es decir cuando ya haya terminado  de recorrer todo el texto osea el texto "email" o siendo mas generales cuando ya haya ejecutado todas las vueltas del bucle y este no devuelva nigun valor ingresaremos en el else.
    
    #En este caso si se ingresa un correo que no contenga el @ niguna iteracion entrara en el if y por lo tanto el bucle no devolvera nada por lo que ingresa en el else devolviendo el False, caso contrario si se ingresa un @ en el correo.
    arroba = False

print(arroba)

