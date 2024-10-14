# 3. OPERADORES LOGICOS "AND" Y "OR": ESTOS OPERADORES SON MUY UTILES PARA HACER COMPARACIONES MAS COMPLEJAS

    #ejemplo de asignacion de beca a estudiante usando and y or como ejemplo

"""
print("Programa de becas año 2024")

distancia_escuela = int(input("Ingrese la distancia a la escuela en Km: "))
print(distancia_escuela)

numero_hermanos= int(input("Ingrese el numero de hermanos: "))
print(numero_hermanos)

salario_familiar = int(input("Ingrese el salario anual bruto de la familia: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

"""

# 4. OPERADOR "IN": ESTE OPERADOR ES MUY UTIL PARA HACER COMPARACIONES MAS COMPLEJAS
    

    #ejemplo de asignacion de beca a estudiante usando in como ejemplo

print("Asignaturas optativas año 2024")
print("Informatica basica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Ingrese la asignatura que desea: ") #tambien el .lower() se puede agregar al final del input quedando de la siguiente menera opcion = input("Ingrese la asignatura que desea: ").lower()

asignatura = opcion.lower()

if asignatura in ("informatica basica", "pruebas de software", "usabilidad y accesibilidad"):

    print("Asignatura elegida: " + asignatura)

else:
    print("Asignatura escogida no encontrada")

#PYTHON ES CASE SENSITIVE, ES DECIR DISTINGUE ENTRE MAYUSCULAS Y MINUSCULAS. PARA SOLUCIONAR ESTO SE USAN LAS FUNCIONES .lower() Y .upper() se usan al final de lo que se quiere convertir en  minuscula o mayuscula