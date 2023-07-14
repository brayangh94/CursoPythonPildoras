#CONCEPTO DE PARAMETRO-ARGUMENTO

# def suma(num1, num2):
 	#le estamos pasando parametros a la funcion
# 	print(num1+num2)

# suma(5,3)
# suma(9,56)
# suma(999,69)

#AQUI USAREMOS EL RETURN
def suma(num1, num2):
	resultado= num1+num2
	return resultado

# print(suma(5,3))
# print(suma(9,56))
# print(suma(999,69))

almacena_resultado= suma(5,8)
# con return se nos permite almacernar en una variable el resultado de una funcion
# esto nos permiter almacenar todo lo que devuelva una funcion en una variable en otro lugar del codigo lo que es muy util
print(almacena_resultado)

#python hace el paso de parametros simpre por referemncia, para paython todos los parametros son referencias