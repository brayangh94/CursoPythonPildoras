#QUE SON LOS DICCIONARIOS : es lo mismo que un array asociativo en php

#son estreucturas de datos parecidos a las lista y a las tuplas , permite almacenar todo tipo de datois (entero, cadena, decimal) , incluso listas, tuplas y otros diccionarios.

#la principal caracteristica de los dicxcionarios es que a la hora de almacenar los datos en el diccionario se hace con una asociacion de tipo clave:valor, es to lo que quiere decir, es que para cadas valor que se almacene en un diccionario se el asigna una clave uncia, NO IMPORTA EL ORDEN CON EL QUE SE ALMACENAN LOS DATOS EN UN DICCIONARIO

#LOS DICCIONARIOS SE DECLARAN DE LA SIGUIENTE MANERA

midiccionario={"alemania":"berlin", "francia":"paris","reino unido":"londres", "españa":"madrid"}

#para acceder a un elemento cocreto de ese diccionario tendremos que preguntarle por la clave, accediendo a la clave obtendremos el valor

print(midiccionario["francia"])

#si se quiere obtener un diccionario entero es de la siguiente manera

print(midiccionario)

#COMO AGREGAR MAS ELEMENTOS A UN DICCIONARIO YA CONTRUIDO

midiccionario["italia"]="lisboa"
print(midiccionario)

#PARA CAMBIAR EL VALOR ASIGNADO A UN CLAVE COMO POR EJEMPLO EN ESTE CASO QUE LA CAPITAL DE ITALIA NO ES LISBOA SE HACE SIMPLEMETE SOBREESCRIBIENDO

midiccionario["italia"] = "roma" #cuando se asignana varios valores a una misma clave esos vaslores se van sobrescribiendo

print(midiccionario)

#para eleminar u nelemento del diccionario se usa la funcion del

del midiccionario["reino unido"]

print(midiccionario)

#los diccionars tambien pueden contener varios tipos de datos

midiccionario2={"alemania":"berlin", 23:"jordan", "mosqueteros":3}

print(midiccionario2)

#otra funcionalidad que se puede hacer es usar las tupla para asignar las claves a cada uno de los valores

mitupla=["alemania", "francia","reino unido", "españa"]

#ahora para que el diccionario tome la tuple y les asigne las claves a cada uno de los valores

midiccionario3= {mitupla[0]:"berlin",mitupla[1]:"paris",mitupla[2]:"londres",mitupla[3]:"madrid"}

print(midiccionario3)

#para acceder a cada valor del diccionario havarias manera

print(midiccionario3["alemania"])
print(midiccionario3[mitupla[1]])

#PARA QUE UN DICCIONARIO AlMACENE UNA TUPLA

midiccionario4 = {23:"jordan", "nombre":"michael", "equipo":"chicago", "anillos":[1991,1992,1993,1996,1997,1998]}

print(midiccionario4)

#otra cosa que se puede hacer es guardar un diccionario en un diccionario 

midiccionario4 = {23:"jordan", "nombre":"michael", "equipo":"chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(midiccionario4.keys()) #EL METODO DEVUELVE TODAS LAS CLAVES de un diccionario

print(midiccionario4.values()) #EL METODO DEVUELVE TODOS LOS VALORES de un diccionario
print(midiccionario4.leng()) #EL METODO DEVUELVE el tamaño de un diccionario la cantidad de clavevalor que hay

