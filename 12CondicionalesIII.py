# VEREMOS SWITCH, CONCATENADORES DE OPERADORES DE COMPARACION, OPERADORES LOGICOS "AND" Y "OR", OPERADOR "IN"

# 1. SWITCH NO ESTA DISPONIBLE EN PYTHON YA QUE DECIDIERON PRENCINDIR DE ELLA, ESTA SEUSA CUANDO SE TIENEN QUE HACER MUCHAS COMPARACIONES. PERO A PESAR DE ESTO  TENEMOS OTRAS HERRAMIENTAS QUE NOS PERMITEN HACER LO MISMO SIN MUCHO ESFUERZO, PUEDE SER UNO DE ELLOS USANDO DICCIONARIOS O LAS SIGUIENTES OPCIONES:


# 2. CONCATENADORES DE OPERADORES DE COMPARACION: PYTHON PERMITE USAR LOO CONCATENACION DE OPERADORES LO CUAL NOS PERMITE EVALUAR MUCHAS CONDICIONES CONCATENADAS.

"""
edad = 7
if 0 < edad < 100: #esto es concatenacion de opradores de comparacion
    print("La edad es correcta")
else:
    print("La edad es incorrecta")
    
"""

#OTRO EJEMPLO

salario_presidnete = int(input("Ingrese el salario del presidente: "))
print("El presidente tiene un salario de: " + str(salario_presidnete))

salario_director = int(input("Ingrese el salario del director: "))
print("El director tiene un salario de: " + str(salario_director))

salario_jefe_area = int(input("Ingrese el salario del jefe de area: "))
print("El jefe de area tiene un salario de: " + str(salario_jefe_area))

salario_administrativo = int(input("Ingrese el salario del administrativo: "))
print("El administrativo tiene un salario de: " + str(salario_administrativo))


if salario_administrativo < salario_jefe_area < salario_director < salario_presidnete: #El inf lee la condiciones concatenadas de izquierda a derecha y va evaluando que todas se cumplen priemro evalua salario_administrativo < salario_jefe_area y asi sucesivamente
    print("Todo funciona correctamente")
else:
    print("Algo no funciona correctamente, algo huele malito")


#como python es un lenguaje fuertemente tipado no se puede concatener un valor de string con un entero, con proejemplo "edad: " + 40 esto no se podria.