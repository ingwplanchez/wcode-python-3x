
# Ejercicios con estructuras repetitivas.

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

## Hacer un programa que imprima todos numeros naturales que hay desde la
## unidad hasta un numero que introducimos por teclado

################################################################################

## Estudio previo:

##  Se requiere una variable para guardar el numero introducido por teclado.
##  Se deben empezar a imprimir los numeros desde el 1 hasta el valor intro-
##  ducido por teclado
##
##  El proceso de introducir un numero es el siguiente:
##
##    - Antes del Ciclo: Para saber hasta que numero debemos imprimir
##    - Fuera del ciclo: Para que solo se pida una vez


################################################################################

## Variables

##  numero = variable para introducir un numero
##  contador = variable para generar e imprimir los numeros

# Pseudocodigo:

##    numero = 0
##    contador = 1
##
##    imprime "Introduce un numero: "
##    introduce numero
##    Hacer mientras contador <= numero
##        contador = contador + 1
##        imprime contador
##    fin del hacer
##    fin del programa

################################################################################

# Declaracion de variables:

int_Numero = 0
int_Contador = 1

################################################################################

# Inicio del programa:

int_Numero = int(input('Introduce un numero: '))

while int_Contador <= int_Numero:

    print(int_Contador)
    int_Contador = int_Contador + 1


################################################################################

## ENUNCIADO 2:

## Introducir tantas frases por teclado como deseemos y contarlas

################################################################################

## Estudio previo:

##    Las frases estan formadas por letras y numeros
##    el proceso para introducir frases es repetitivo por lo tanto ira dentro
##    del bucle.

################################################################################

## Variables

##    respuesta = para preguntar si queremos introducir mas frases
##    frase = almacena la frase
##    contador = variable para contar el numero de frases

# Pseudocodigo:

##    respuesta = 'S'
##    frase = ""
##    contador = 0

##    Hacer mientras respuesta == 'S'
##        imprime "Introduce una frase: "
##        introduce frase
##        contador = contador + 1
##        imprime "Deseas introducir mas Frases (S/N): "
##        introduce respuesta
##    fin del Hacer
##
##    imprime "El numero de frases introducidas son: "
##    imprime "Contador"
##
##    fin del programa

################################################################################

# Declaracion de variables:




################################################################################

# Inicio del programa:




################################################################################

