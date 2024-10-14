#Tipo range() y las notaciones especiales con print()

"""
for a in range(5):
    #una manera de imprimir valores de variables dentro del print seria de la siguiente manera, usando la funcion de tipo que nos permiten trabajar con formatos de forma diferente.
    print(f"El valor de la variable es: {a}")
"""


#En otro lenguajes Un bucle for for pudue recorrer un valor numerico de adelante hacia atras, o de un valor determinaod a otro, no impre s etiene qu partir desde el cero, aqui en pytho podeos ayudarnos con el tipo range() para lograr esto.
    
    #El range() nos permite crear un rango de valores numericos, en este caso desde el 5 hasta el 50, peor tambien adminte un tercer argumento que es de cuanto en cuanto va air ese contemos en este caso ira de 3 en 3.
for a in range(5,50, 3):
    print(f"El valor de la variable es: {a}")


valido = False

email=input("Ingrese su email: ")

for i in range(len(email)):
    #en este caso en range no esta recorriendo valores dados, sino simplemente un len() que nos devulve la cantidad de caracteres que tiene un strung.
    if email[i] == "@":
        valido = True

if valido:
    print("El email es valido")
else:
    print("El email no es valido")