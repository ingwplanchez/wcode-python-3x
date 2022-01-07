
# Interruptor o bandera

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

## TEORIA:

##   Una bandera o flag es una variable que solo puede tomar dos valores 0 o 1.
##   por este motivo tambien son llamadas interruptores para indicar:
##
##   Encendido o apagado
##
##   Se utilizan para saber si el programa ha pasado por un determinado punto
##   y variar la secuencia de ejecucion de un programa dependiendo del valor
##   que poseen en cada instante.

################################################################################

## ENUNCIADO:

## Imprimir 10 veces de una forma alternativa 'Hola' y 'Adios'

################################################################################

## Estudio previo:

##    Necesitaremos un contador para imprimir la serie de numeros del 1 al 10
##
##    La visualizacion de una forma alternativa de dos comentarios diferentes
##    la hacemos mediante una bandera.
##
##    La bandera permite saber segun su valor 0 o 1, si la última palabra fue
##    'Hola' o 'Adios'
##
################################################################################

## Variables:

##    bandera = para saber si acabamos de imprimir Hola o Adiós
##    contador = variable para contar del 1 al 10

#   Pseudocodigo:

##    bandera = 0
##    contador = 0
##
##    Hacer mientras  contador <= 10
##        if bandera = 0
##            imprime "Hola"
##            bandera = 1
##        else
##            imprime "Adios"
##            bandera = 0
##        fin del if
##        contador = contador + 1
##    fin del Hacer
##    fin del programa

################################################################################

# Declaracion de variables:


################################################################################

# Inicio del programa:
