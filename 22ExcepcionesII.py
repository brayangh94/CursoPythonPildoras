# Veremos como capurar varias exceciones de forma simultanea

# veremos la clausula Finally

#En un programa se pueden comenter errores de muchos tipos, nosotros corregimos el error de la divicion entre cero, pero pueden haber muchos mas.

# si por ejemplo al ingresar los valores numericos para operar con ellos en luga rde numero agregamos texto, ps no dara un error de tipo ValueError.

"""
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplican(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError: #este es el error que da al dividir entre cero
        print("No se puede dividir entre 0")
        return "Operacion erronea"

while True:
    try:
        op1=int(input("Ingrese el primer numero: "))

        op2=int(input("Ingrese el segundo numero: "))#De esta manera usando el bucle, al introducir los valores correctamente no pasa nada y rompo el bucle con el break y todo sigue normal, pero se se introducen valore serroneos, pasa al except y vuelve a la siguiente vuelta del bucle. Si no se hiciera de esta menera luego de dispararse la excepcio el programa seguiria y pediria que ingrese la operacion caa que dispararia otro error ya que no se llenaron los valores de op1 y op2
        break

    except ValueError:
        print("Los valores introducidos no son correctos. Por favor agrega valores numericos")


operacion=input("Ingrese la operacion (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplican(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

"""

# Ahora haremos una unica funcion de ejemplo solo para dividir, pero estara construida de una manera diferete, no recibira ningun argumento, y la funion va a realizar todo el trabjao, va a pedir los valores numericos, va a realizar el calculo y ava a imprimir el calculo y va a lanzar un mensaje final de calculo finalizado, todo lo va a hacer la funcion.

def divide():
    # este bloque de codigo que se encuentra dentro de la funcion es suceptible a caer en varios errores, por lo que se debe manejar el manejo de la excepcion de una manera diferente, lo haremos de forma consecutiva.
    
    try:
        op1=float(input("Ingrese el primer numero: "))
        op2=float(input("Ingrese el segundo numero: "))

        print("El resultado de la division es:", op1/op2) #esta es la forma de imprimir el calculo con variables

    #python permite manejar excepciones de manera consecutiva por lo que se podria agregar    
    except ValueError:
        print("Los valores introducidos no son correctos. Por favor agrega valores numericos")
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    
    

    # Tambien se puede hacer un except general (sin colocar nigun valor de error) que se encarga de manejar todos los errores pero esta es una practica poco recomendada ya que no le permite saber al uusario porque fallo.

    finally:# cuando quieres que algo se ejecute si o si, se suele usar la clausula finally.
        #esta clausuala es muy usada para cuando necesita que pase lo que pase se ejecute un fracmento de  codigo, como por ejemplo cuando estas haciend conusltas a bases de datos se cirre la conexion con la base de datos par aque no quede abierta
        print("Calculo finalizado")
divide()