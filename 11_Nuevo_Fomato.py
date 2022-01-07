
# Nuevo Formato

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
#############################################################################

# Descarga de Pyscripter:
# https://sourceforge.net/projects/pyscripter/files/

str_Lenguaje1 = "Pseudocodigo"
str_Lenguaje2 = "Python"

# cadena.format(): Permite Formatear la cadenas

str_Centro = " METODO FORMAT() "

print("\n" + str_Centro.center(80, "-") + "\n")

print("1) El lenguaje es {0}.\n".format(str_Lenguaje1))

print("2) Los lenguajes son: {0} y {1}.\n".format(str_Lenguaje1,str_Lenguaje2 ))

print("3) Los lenguajes son: {} y {}.\n".format(str_Lenguaje1,str_Lenguaje2 ))

print("4) Los lenguajes son: {a} y {b}.\n"
.format(a = str_Lenguaje1 ,b = str_Lenguaje2))

print("5) Intercalado: {0} , {1} , {0} , {1}.\n"
.format(str_Lenguaje1,str_Lenguaje2 ))

#############################################################################
