
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

int_Numero = 0

################################################################################

# Inicio del programa:

# SOLICITUD Datos en PYTHON 2.7
# int_Numero = int (raw_input('Introduce un numero: '))

# SOLICITUD de Datos en PYTHON 3.x
int_Numero = int(input('Introduce un numero: '))

if int_Numero == (int_Numero / 3) * 3:
    print("El numero %d es par." %(int_Numero))
else:
    print("El numero %d es impar." %(int_Numero))

