
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

# Instruccion FOR IN:

# 	PARA CADA ELEMENTO HACER
#		instrucciones
# 	FIN del HACER

# Ejemplo:

Mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']

str_Cadena = " BUCLE FOR IN "
print("\n" + str_Cadena.center(35, "*") + "\n")

for nombre in Mi_lista:
    print(nombre)

#############################################################################

# Pseudocodigo:

# Instruccion WHILE:

# 	HACER MIENTRAS condicion
#		instrucciones
# 	FIN del HACER

# Ejemplo:

int_Indice = 0

str_Cadena = " BUCLE FOR IN CON UN WHILE "
print("\n" + str_Cadena.center(35, "*") + "\n")

while int_Indice < len(Mi_lista):
    print(Mi_lista[int_Indice])
    int_Indice = int_Indice + 1

