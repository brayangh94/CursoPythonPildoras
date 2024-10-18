#Las excepciones son errorres en tiempo de ejecucion. Cuando se tiene un programa correctamtne esrito, pero ocurre de igual manera   un error inesperado, cuando ocurre esto no se ejecutaran las lineas de codigo siguiente despues de la linea donde se ha generado el error.

try:
    print("Hola")

except :#aqui antes de los dos puntos (:) iria el nombre del error de la exceocion, solo si falla por el nombre del error que se indica en el except la lectura del codigo continuara, si falla por otro error el codigo se detendra y mostrara direcamente el error.
    print(" mensaje que indique que hubo un error")

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
        #En el excep antes de los dos puntos (:) yl uego del excep iria el nombre del error de la exceocion (en este caso es ZeroDivisionError), solo si falla por el nombre del error que se indica en el except la lectura del codigo continuara, si falla por otro error el codigo se detendra y mostrara direcamente el error.
        print("No se puede dividir entre 0")
        return "Operacion erronea"

op1=int(input("Ingrese el primer numero: "))

op2=int(input("Ingrese el segundo numero: "))

operacion=input("Ingrese la operacion (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplican(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))
