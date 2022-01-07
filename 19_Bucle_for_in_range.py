
# Bucle infinito

# ESTILO WCODE

# Variables
# int_Nombre_variable = tipo_dato       ;   Variables del tipo entero
# float_Nombre_variable = tipo_dato     ;   Variables con decimales
# str_Nombre_variable = tipo_dato       ;   variables con Cadenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   variables booleanas

# Constantes
# const_NOMBRE_CONSTANTE = tipo_dato    ;   Constante de cualquier tipo de datos
# NOMBRE_CONSTANTE = tipo_dato

# Colecciones
# list_Nombre_Lista = [dato1,dato2,...]         ;   Elementos de una lista
# tuple_Nombre_tupla = (dato1,dato2,...)        ;   Elementos de una tupla
# dic_Nombre_diccionario = {'clave':dato2,...}  ;   Elementos de un diccionario
#

# Usos especiales de las variables

# Contadores
# Variable  = Variable +/- CONSTANTE

# Acumuladores o Sumadores
# Acumulador = Acumulador +/- Variable)

#############################################################################

# Pseudocodigo:

# Instruccion FOR IN RANGE:

# 	PARA CADA ELEMENTO EN EL RANGO HACER
#		instrucciones
# 	FIN del HACER

# Ejemplo:

str_Cadena = " BUCLE FOR IN RANGE "
print("\n" + str_Cadena.center(70, "*") + "\n")

numero = int(input('Intruduce el numero a elevar: '))

for potencia in range(0,11):
    resultado= numero ** potencia
    print("%d elevado a %d es %d")%(numero,potencia,resultado)

#############################################################################

# Pseudocodigo:

# Instruccion WHILE:

# 	HACER MIENTRAS condicion
#		instrucciones
# 	FIN del HACER

# Ejemplo:

potencia = 0

str_Cadena = " BUCLE FOR IN RANGE CON UN WHILE "
print("\n" + str_Cadena.center(70, "*") + "\n")

while potencia >= 0 and potencia  < 11:
    resultado= numero ** potencia
    print("%d elevado a %d es %d")%(numero,potencia,resultado)
    potencia = potencia + 1

