# LAS LISTAS

# NOTA = para ejecutoar el codigo y ver lo que hace en la consola es con control B en sublimeText

#DEFINICION Y CARACTERISTICAS

#son el equivalente a los arreglos, vectores en otros lenguajes, o por lo menos son muy parecidos y la utilidada si iviene a ser la misma

#por lo tanto las listas en python on esructuras que nos permiten almacenar varios valores en unsa sola variable

#las listas en python no permitan guardar diferentes tipos de valores, esto no es asi en otro lenguajes de programacion  

# las listas se pueden expandir dinamicamente en python lo cual es muy comodo

#SINTAXIS

# nombreLista=[elem1,elem2,elem3,.....]

#los elemento que forman parte de la lista deben estar identificados y localizables lo que se logra con un indice que es, la pocision de lelemnto dentro de la lista, la preimera posicion siempre es cero 0 y el siguiente 1 y asi sucesivamente

#veremos como crear una lista, como agraar elementops de forma dinamica, eliminar elementos, accedr aun elemento en croncreto paandonos su indice, etc.

#ejemplo de declaracion de lista
miLista=["rosa", "elisa", "brayan", "ivan"]

#para acceder a  mostar esta lista se hace de la siguente manera

print(miLista[:])
#para acceder a todos los elementos se colocan dos puntos dentro de los corchetes

#si se quiere acceder al elemento que esta en la pocicion 2 se hace comlocando su indice entre los corchetes

print(miLista[2])
#si se pusieran indices negativos, python interpretaria eso como que se esta contan los indices del final hasta el inicio pero con la diferencia que al pasarle indice negativo la cuanta no empesaria en 0 sino en -1, por lo tanto -1=ivan, -2=brayan, -3=elisa, -4=rosa

#CUANDO SE TENGAN LISTAS MUY LARGAS: es muy probable que debamos acceder a lo que se conoce como una porcion de lista, que como se olle es aaceder solo a una parte de esa lista 

print(miLista[0:3])#esto significa que accedera a la lista desde el indice 0 osea incluyendo el indice 0 hasta el indice 3 osea hasta antes del indice 3 excuyendo el indice 3 y los siguintes

print(miLista[:3])#si voy a empesar por el indice 0 no es necesario indicarlo porquer python sobre entiende

print(miLista[2:])#otra manera es como se muestra en esta linea y lo que esta indicando e sque acceda a los dos ultimos elementos, que seria desde el inde 2 hasta el final




# PARA AGREGAR ELEMENTOS A UNA LISTA  se debe usar la funcion .append(), esta los va agregando en la ultima posision

miLista.append("gloria")

print(miLista[:])

# y si se quisiera agragar un elementos en cualquir posicion de la lista se usria, .insert(indice de la posicion en la que quiere agrar,elemento que se quiere agregar)

miLista.insert(2, "juana")

print(miLista[:])

#si se quisiera agregar varios elementos a la lista se usa .extend(["elemen1","elemen2","elemen3"])

miLista.extend(["juano", 5, False, 3.6, "brayan"])#True o false si se van a escribir empiezan en mayusculas

#en la linea anterior se pudo ver como las listas trabajan a las vez con diferentes tipos de datos

print(miLista[:])


#PARA QUE SE NOS DEVUELVA EL INDICE DE UN ELEMENTO DENTRO DE UNA LISTA

 #seria con la funcion .index(elementos que se encuenta en ese indice)

print(miLista.index("brayan"))
#si hubiera 2 elemtos en la lista con el mismo nombre o valor, .index devolveria un valor, el numero del indice del primero de ellos que encuentre primero

#COMPROBAR SI UN ELEMENTO SE ENCUENTRA O NO SE ENCUENTRA EN UNA LISTA: con el elemento "in" , devolvera un true o false si el elemento s eencuentra en la lista

print("rosa" in miLista)

#PARA ELIMINAR ELEMENTOS SE USA LA FUNCION: .remove(aqui ira el valor del elemento a eliminar, sea un estream, un booleano o numero)

miLista.remove(5)

print(miLista[:])

#tambien contamos con .pop cuya funcion es eliminar el ultimo elemento de una lista

miLista.pop()
print(miLista[:])

#si se quisieran unir 2 listas que ya existen , se haria usando el operador suma + de la siguiente manera

miLista2=["sara","maria"]

miLista3 = miLista + miLista2

print(miLista3[:])

#otro operador que funciona con las listas es el operador multiplicxacion que lo que hace es hacer que en una lista se repitan sus elementos el numero de veces por el que se multiplique, se puede multiplicar tanto en la declaracion de la lista como en la impresion de ella

print(miLista2[:]*3)