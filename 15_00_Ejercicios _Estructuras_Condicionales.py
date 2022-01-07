
# Ejercicios con estructuras condicionales

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

## ENUNCIADO 1:

##
##    Introducir un numero por teclado y que se muestre un mensaje indicando
##    si es par o impar.

################################################################################

## Estudio p.revio:
##
##    Para saber si un numero es par o impar haremos lo siguiente:
##
##    FORMA 1:
##
##    Numero = int(Numero/2)*2
##
##    - Si resulta el mismo numero el numero es par.
##    - Si no es el mismo numero no es par.
##
##    FORMA 2:
##
##    Numero = Numero % 2
##
##    - Si el modulo de la division es 0 el numero es par
##    - Si el modulo de la division es diferente de 0 es impar

################################################################################

## Variable
## numero = almacena un numero introducido por teclado

# Pseudocodigo:

##    numero = 0

##    imprime "Introduce un numero:"
##    introduce numero
##
##    if numero = int(numero/2)*2
##        imprime "El numero es par"
##    else
##        imprime "El numero es impar"
##    fin del if
##    fin del programa

################################################################################

# Declaracion de variables:

int_Numero = 0

################################################################################

# Inicio del programa:

int_Numero = int(input('Introduce un numero: '))

if int_Numero == (int_Numero / 2) * 2:
    print("El numero %d es par." %(int_Numero))
else:
    print("El numero %d es impar." %(int_Numero))

################################################################################

## ENUNCIADO 2:

##    Introducir un numero por teclado y que se muestre un mensaje indicando
##    si es multiplo de 3.

################################################################################

## Estudio previo:

## Vamos a proceder de forma analoga al ejercicio anterior esta vez dividiendo
## entre 3.

##    FORMA 1:
##
##    Numero = int(Numero/3)*3
##
##    - Si resulta el mismo numero el numero es multiplo de 3.
##    - Si no es el mismo numero no es multiplo.
##
##    FORMA 2:
##
##    Numero = Numero % 3
##
##    - Si el modulo de la division es 0 el numero es multiplo
##    - Si el modulo de la division es diferente de 0 es multiplo

################################################################################

## Variable

## numero = almacena un numero introducido por teclado

# Pseudocodigo:

##    numero = 0

##    imprime "Introduce un numero:"
##    introduce numero
##
##    if numero = int(numero/3)*3
##        imprime "El numero es multiplo de 3"
##    else
##        imprime "El numero no esmultiplo de 3"
##    fin del if
##    fin del programa

################################################################################

# Declaracion de variables:

################################################################################

# Inicio del programa:



