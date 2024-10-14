#Tipos de bucles

# tenemos lo bucles determinados y los indeterminados

#Los bucles determinados son los que se ejecutan un numero determinado  de veces. (Se sabe a priori cuantas veces se va ajecutar un codigo del interiro del bucle) en python el bucle determinado es el bucle for

#Los bucles indeterminados son los que se ejecutan de manera indefinida n cantidad de veces, (el numero de veces que se ejecutara dpeendera de las circunstancias durante la ejecucion del programa)

        #bucle For

# el bucle for se declara de la siguiente manera

for i in ["primavera", "verano", "otoño", "invierno"]:  #el elemento a rrecorrer puede ser una lista ,una tupla, un rango, etc
    #el bucle for se ejecutara tantas veces como elementostenga el elemento que esta recorriendo el bucle for

    # El funcionamiento interno del bucle for es que a la variable i se le asignara el primer elemento de la lista en este caso "primavera", eh imprime o jecuta todo lo que haya en el interior del bucle y despues se le asignara el segundo elemento de la lista "verano" y asi sucesivamente hasta que se llegue al ultimo elemento de la lista que es "invierno".

    #cuando el bucle llega al final de los elementos de la lista que esta recorriendo se sale del bucle.
    print("hola")

    print(i)