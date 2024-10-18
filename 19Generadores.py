    # Los Generadores son estructuras queextraen valores de una funcion de una manera diferente acomo estamos aostumbrados a hacerlo en otros lenguajes, y esos valores que se extraen la la funcion se van a almacenar en objetus iterables, por lo que esos valores lso vamos a poder recorrer, con bucles (for, while) o incluso con otras estructuras que en este punto aun no se han visto como por ejemplo iteradores o el metodo next().

    # Esos valores se almacenan de uno en uno dentro del generador.

    #Cada vez que se almacene un valor, el egenerador permanecera es un estado de stand by hasta qye se solicite el siguiente valor. este estado de stand by se llama "Suspencion de estado"

    #esto funciona de tal manera que se hace la llamada a la funcion y se va a realizar la tarea que devolvera el valor correspondiente, peor la funcion debe devolver un conjunto de valores devolvera el primer valor, creara un objeto la funcion netrara en standby y se va a almacenar en memoria, y luego se va a llamar a la funcion nuevamente y se va a realizar la tarea que devolvera el segundo valor, y asi sucesivamente.

    #la funcionalidad o ventaja que puede tener esto es que obtengamos los valores de una lista de uno en uno en lugar de todos los valores a la vez de golpe. Las ventajas de este comportamiento son:

        #Son mas eficientes que las funciones tradicionales: porque bajo determinada situaciones cuando requerimos que nos devuelva los valores de 1 en 1 para reaalizar la busqueda de un valor, cuando no queremos gastar recursos en almacenar los valores que no nos interesan luego de haber encontrado el valor que nos interesa.

        #Son muy utiles con listas de valores infinitos: Por ejemplo una funcion que tiene que generar  funciones IP al azar. Ademas de muchas otras funcionalidades.





#haramos un ejemplo generando una lista de numeros pares y lo haremos con una funcion tradicional y luego con un generador para ver su difierencias:

#esta es la funcion tradicional:
"""
def generador_pares(limite):

    num = 1
    miLista=[]

    while num < limite:

        miLista.append(num*2)

        num += 1

    return miLista

print(generador_pares(10))
"""

#esta es el generador:

#como el mismo generador nos va a devolver lo la lista en un objeto iterable ya no nocesitariamos la lista (miLista) que defini en la funcion anterior y no se usaria la instruccion return, hay ocaciones en el que la instruccion retur se usa en generadores pero se vera mas adelante.

"""
def generador_pares(limite):

    num = 1


    while num < limite:

        yield num*2     

        num += 1

#como yield nos devuelve un objeto iterable qu esera donde se iran cargando los valores necesitamos una variable objeto donde se pueda guardar el objeto iterable que devuelve el generador.

devulevePares = generador_pares(10)

#luego de tener oe onjeto iterable solo queda recorrerlo con un bucle for o while:

for i in devulevePares:

    print(i)
"""


#ahora imaginemonos que no queremos que el generador nos devuelva todos los valores de la lista, solo queremos que nos devuleva o mejor dicho mostrar los 3 primeros elementos.

#En ese caso en lugar de recorrer el objeto iterabla con un for, lo que se hara es decirle al programa que os muestre valor a valor lo que el objeto tiene almacenado en su interiror y para eso se va autilizar el metodo next().
    
def generador_pares(limite):

    num = 1


    while num < limite:

        yield num*2     

        num += 1


devulevePares = generador_pares(10)

print(next(devulevePares))

#El valor recibido por next() es utilizado como si fuera el resultado de la iteración anterior (último valor entregado por yield )

print("Aqui podria ir mas codigo......")

devulevePares = generador_pares(10)

print("Aqui podria ir mas codigo......")

devulevePares = generador_pares(10)

#entre llamada y llamada de la funcion el generador el generador entra en un estado de suspencion, este estado de sus pencion hace que se ahorren recursos.
