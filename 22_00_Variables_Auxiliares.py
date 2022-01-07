
# Variables auxiliares

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

## ENUNCIADO:

##    Introducir dos numeros naturales por teclado. Imprimir los numeros
##    naturales que hay entre ambos numeros empezando por el mas pequeñp.

################################################################################

## Estudio previo:

##    Supongamos que introducimos por teclado los numeros 5 y 20 no importa
##    el orden.
##
##    La impresion de los numeros la realizamos mediante un ciclo con dos
##    variablesque contengan al menor y al mayor de los numeros, y un contador
##    que vaya desde el numero inferior al superior.
##
##    El problema es saber cual es el menor si el primero o el segundo. Si el
##    mayor es el numero introducido en primer lugar debemos intercambiar los
##    numeros con una variable auxiliar.
##
##    Ejemplo:
##
##            menor = 20
##            mayor = 5
##            aux = 0
##
##        Volcamos el contenido de una de las variables en auxiliar:
##
##        aux = menor
##
##        El panorama queda de la siguiente manera
##
##            menor = 20
##            mayor = 5
##            aux = 20
##
##        El contenido de 'mayor' los volcamos en menor:
##
##        menor = mayor
##
##        y la situacion es:
##
##            menor = 5
##            mayor = 5
##            aux = 20
##
##        por ultimo se asigna a 'mayor' el contenido de la variable auxiliar.
##
##        mayor = aux
##
##        quedando los siguientes valores:
##
##            menor = 5
##            mayor = 20
##            aux = 20
##
##        en resumen el proceso será:
##
##            aux = menor
##            menor = mayor
##            mayor = aux
##
################################################################################

## Variables:

##    num1 = recoge el primer numero introducido por teclado.
##    num2 = recoge el segundo numero introducido por teclado.
##    aux = variable auxiliar para realizar el intercambio de los numeros
##          si num 2 es mas pequeño que num1.

#   Pseudocodigo:

##    num1 = 0
##    num2 = 0
##    aux = 0
##
##    imprime "Introduce el primer Numero"
##    introduce num1
##    imprime "Introduce el segundo Numero"
##    introduce num2
##
##    if num1 > num2
##        aux = num1
##        num1 = num2
##        num2 = aux
##    Fin del if
##
##    Hacer mientras num1 <= num2
##        imprime num1
##        num1 = num1 + 1
##    Fin del Hacer
##    Fin del programa


################################################################################

# Declaracion de variables:

################################################################################

# Inicio del programa:

