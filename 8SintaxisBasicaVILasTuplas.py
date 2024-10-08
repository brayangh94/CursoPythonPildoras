#LAS TUPLAS

#las tuplas son listas inmutables, es decir no se pueden modificar luego de su creacion.

#no permiten añadir, remover, eliminar elementos(no se podria usar append, extend,remove)

# si permiten extraer porciones, pero el resultado de esa extraccion es una nueva tupla.

#las tuplas no permiten realizar busquedas (no se podra usar index) / AHORA SI LO PERMITE

# pero si es permitido comprobar si un elementos esta en la tupla, osea se busca el valor que se requiera, mas no se puede buscar por los indices

#QUE UTILIDAD TIENEN LAS TUPLAS POR ENSIMA DE LAS LISTAS:

#las tuplas son mas rapidas a la hora de ejecutarlas por las optimizaciones que tienen

#ocupan menos espacio , tiene mas rendimiento, (si se necesitara guardar una lista de elementos que que no va a ser modificada y solo se va a recorrer , entoces es mejor una tupla que una lista)

#permiten formatear cadenas de caracteres 

#pueden utilizarse como claves en un diccionario (las listas no se pueden usar para esto)



#COMO DECLARAR LAS TUPLAS

#a la vez que las listas se declaran con corchetes[], las tuplas se declaran con parentesis () ó no tener estar encerrados en nada, solo para el caso de las tuplas 

#nombreTupla=(elem1,elem2,...,etc) , el indice de las posiciónes tambien empiezan en cero 0 como las listas, las listas se declaran en parentesis , pero a la hora de leer sus valores con el indice si se hace con corchetes []

miTupla=("Brayan",12,11,1994)

print(miTupla[2])

#EXISTEN 2 METODOS PARA COMBERTIR LISTAS EN TUPLAS Ó TUPLAS EN LISTAS

#para convertir una tupla en una lista tenemos el metodo list()

miLista=list(miTupla)

print(miLista)

#para convertir una lista en tupla se usa el metodo tuple()

miLista2=["ivan",2.2,3000,565]
miTupla2=tuple(miLista2)

print(miTupla2)

#para ver si un elemento se encuentra en una tupla se usa la instruccion in, la cual devolvera un booleano

print("ivan" in miTupla2)

#para saber la cantidad de elementos que hay con el valor que se esta buscando en una tupla , se usa el metodo count()

print(miTupla2.count(3000))

#para saber que tan grande es una tupla se usa el metodo len()

print(len(miTupla))#OJO esto no da el ultimo indice da el numero de elemntos que hay, para tenr el indice se le restaria 1 al valor que devuelva

#tambien se pueden crar tuplas unitarias, que son tuplas con un solo elemento, para que sean unitarias, luego de declarar su unico valor se debe poner una coma ,

miTuplaUnitaria=("hola",)

#cuando se declaran tuplas tambien se puede precindir de los parentesis

miTuplaSinParentesis="holanda", 56, 96, "chaolines"#declararla de esta manera se conoce como empaquetado de tupla

print(miTuplaSinParentesis)

#pero tambien tenemos el desempaquetado de tupla, esto permite asignar todos los valores que pertenecen a una tupla a diferentes variables de manera sencilla

mituplaParaDesempaquetar=("juan", 12, 9 ,1995)

nombre, dia, mes, ano = mituplaParaDesempaquetar #y asi de manera simple se desempaqueto la tupla en difernetes variables

print(nombre)
print(dia)
print(mes)
print(ano)

 