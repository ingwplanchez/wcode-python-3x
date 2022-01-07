
# Recursividad de funciones

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

##
## Pseudocodigo:

##  FUNCION:
##        Instruciones
##  Fin de FUNCION

## Instrucciones
## Hacer FUNCION
## Instrucciones

################################################################################

# Declaracion de variables: Globales

################################################################################

## Inicio del Programa:

def clave(int_intento = 1):

    str_respuesta = input("Introduce la clave: ")

    if str_respuesta != "abc123":

        if int_intento < 3:

            print("\nClave incorrecta! Intenta de nuevo")
            int_intento = int_intento + 1
            clave(int_intento) # Llamada recursiva

        else:
            print("\nUsuario Bloqueado!")
    else:
        print("\nClave Correcta!")

clave()


