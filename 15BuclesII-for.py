# bucle for

#Recorriendo strings

    #Esto es una axxion que se usa mucho para comparar direcciones de correo electronico o acciones de loggeo de sesion

#Cuando el bucle gor tiene que recorrer un string lo van a hacer caracter a caracter. El bucle se ejecutara con el numero de caracteres que tenga el string.

#entonces el hecho de por recorrer el string caracter a caracter nos permite poder verificar pro ejemplo si un correo electronico es valido.

        #en este ejemplo veirficaremos que si un direccion de correo tiene un @ es correcto, si no lo tiene no es valido.
contador = 0
#email = True
mi_email = input("Ingrese su correo electronico: ")


for i in mi_email:
    if (i == "@" or i == "."):
        contador += 1


#if email: #en este no es necesario poner email == True ya que email es una variable booleana por lo que se puede poner simplemente el true o false 
if contador == 2:
    print("El correo es valido")


else:
    print("El correo no es valido")









# tipo de dato range en python

    # El range es un tipo de dato en python que surgio a partir de la version 3.1, Lo que permite es utilizar el bucle for con conteos numericos algo paracido a como funciona el for en otros lenguajes.

    #el tipo range nos devulenve algo muy parecido a un aray


for i in range(5):
    print("Hola")
    print(i)

    #al imprimir i nos devolvera [0,1,2,3,4]

    #en este caso el range lo que esta haciendo es crear una lista (o serie de elementos que van del 0 al 4) [0,1,2,3,4] y va recorriendo esa lista y va imprimiendo cada elemento de la lista.

    #por lo tanto se imporimira el hola 5 veces








# Notaciones especiales con print utiles en bucles

"""

for i in [1,2,3]:
    #para hacer que el print imprima todo lo que se le  esta agregando en una sola linea, esto se hace agregando el argumento end="" , esto se hace para que el print no imprima un salto de linea al final de la linea de codigo, sino que en lugar agregue en lugar del salto lo que se indique entre las comillas.
    print("HOLA", end=" ")

"""