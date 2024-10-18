# veremos una instruccion que era mas nueva que yield que se agrego a python, en una actualizaicion, llama "yield from"

#cuando utliizamos yield from en un generador lo que logramos es simplificar el codigo del generador en el caso en el que nos veamos obligados a utlizar bucles anidados dentro de este generador, com por ejemplo un for dentro de otro for.

#Con el siguiente ejemplo veremos en que caso se puede necesitar bucles anidados dentro de un generador.

#los elementos que se generan dentor de un geenrador pueden ser texto, numeros, listas, tuplas o diccionarios. Si ele generador devuelve un objeto un ejemento quecontiene valores adentro y deseas acceder al interiror de ese elemento para ver como esta formado para ver los subelementos que forman parte de ese elemento. Bueno python nos simplefica el manejo de bucles anidados con yield form para este caso.

def devuelve_ciudades(*ciudades):

#en pytho cuando se se define una funcion y se indica un * antes del argumento de dicha funcion como en este caso, se le esta undicando al programan que va a recibir un numero indeterminado de elementos es decir no sabemos si va a recibir un elemento, 2 o 10, ademas esos elementos que no sabemos cunntos son los va arecibir en forma de tupla.
    
#ahora imaginemos que queremos acceder a las letras que forman parte de los elementos ps para eso usariamos bucles for anidados
    
    """
    for ciudad in ciudades:
        for letra in ciudad:
            yield letra
    """

    #Pero para simplificar esto se usaria el yield from 
    for ciudad in ciudades:
            yield from ciudad # esto permite no tener que usar el segundo bucle. Ya que permite hacer yield desde el elemento.



ciudades_devuletas = devuelve_ciudades('San Cristobal', 'Merida', 'Trujillo', 'Coro')

print(next(ciudades_devuletas))
print(next(ciudades_devuletas))