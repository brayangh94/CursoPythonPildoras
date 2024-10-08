#veremos la condicions IF

#el condicionla if funciona como en todos los lenguajes de programacion

print("Programa de evaluacion de notas de alumnos")

# Todo lo que ingrese atravez de una funcion input esta considreado como texto por lo que se se va atrabajr con valores nuemericos se debe cambiar a tipo numerico, PARA ESTO USAREMOS LA FUNCION int()


nota_alumno = input("Ingrese la nota del alumno: ")

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "reprobado"
    return valoracion


print(evaluacion(int(nota_alumno)))