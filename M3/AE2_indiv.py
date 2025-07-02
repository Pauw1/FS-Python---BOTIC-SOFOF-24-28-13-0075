# Ejercicio Individual AE2 Módulo 2 de FS-Python 0075 - Alumna Paulina Rojas


# 1. Imprime "Hola, mundo"

print( "Hola mundo!" ) # con comillas dobles

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Paulina"

print( "Hola", nombre ) # con una coma

print( "Hola"+ nombre ) # con un +


# 3. Imprimir "Hola 156!" con el número en una variable

numero = 156

print( "Hola", numero ) # con una coma

# print( "Hola"+ numero ) # con un + -- este debería arrojar un error!, corrígelo con conversión

print( "Hola " + str(numero) ) # con conversión a cadena

# 4. Imprimir "Me encanta comer completos y sushi" con las comidas en variables

comida1 = "completos"

comida2 = "sushi"

print( "Me encanta comer {} y {}" .format(comida1, comida2) ) # con .format()


print( f"Me encanta comer") # con una cadena f