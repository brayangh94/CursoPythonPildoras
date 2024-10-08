
# instruciiones if USANDO TAMBIEN ELSE Y ELIF


print("Verificación de acceso")

#edad_usuario = int(input("Ingrese su edad: "))  

"""
if edad_usuario < 18:
    print("No tiene acceso")

if edad_usuario > 100:
    print("Edad incorrecta")#el else no va a comparar con el primer if sino con este ultimo por lo tanto el programa no funcionaria correctamente. Osea el else es complemto de un if y no de todos.

#El else debe ir siempre acompañado de un if 
else:
    print("Puedes pasar")

print("Fin del programa")
"""

#para hacer que el ejemplo anteriro funcione correctamtne se usa la instrcución elif

"""
if edad_usuario < 18:
    print("No tiene acceso")

elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

print("Fin del programa")
"""

#EN ESTE CASO SI ENTRA EN EL ELSE CUANDO NADA DE LAS CONDICIONES ANTERIORES SE HAN CUMPLIDO Y NO CUANDO NO SE HA CUMPLIDO EL ULTIO IF MAS CERCANO AL ELSE.


#NOTA ALUMNO

nota_alumno = int(input("Ingrese su nota: "))

if nota_alumno < 45:
    print("suspendido")
elif nota_alumno < 50:
    print("suficiente")
elif nota_alumno < 70:
    print("Bien")
elif nota_alumno < 90:
    print("notable")
else:
    print("sobresaliente")

    #EN ESTE ULTIMO EJEMPLO EL BLOQUE DE ELIF FUNCIONARIA BIEN PORQUE APENASSE CUMPLE UNACONDICION SE SALE DE LBLOQUE DE LAS CONDICIONES, POR LO TANTO TODO EL BLOQUE FUNCIONA COMO UNA UNICA EJECUCION TRABAJANDO CON ELIF
