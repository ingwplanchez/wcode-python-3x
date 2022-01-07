
# Estructuras Repetitivas.

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
################################################################################

# Pseudocodigo:

# Instruccion WHILE:

# 	HACER MIENTRAS condicion
#		instrucciones
# 	FIN del HACER

# Ejemplo:

# Declaracion de variables

int_Tabla = 11
int_Numero = 1
int_Resultado = 0

str_Cadena = " TABLA DE MULTIPLICAR "

print("\n" + str_Cadena.center(35, "*") + "\n")

while int_Numero < 101:

    int_Resultado = int_Tabla * int_Numero

    print ("{} x {} = {}").format(int_Tabla,int_Numero,int_Resultado )

    # Contadores
    # Variable  = Variable +/- CONSTANTE

    # Acumuladores o Sumadores
    # Acumulador = Acumulador +/- Variable)

    int_Numero = int_Numero + 1

#############################################################################

