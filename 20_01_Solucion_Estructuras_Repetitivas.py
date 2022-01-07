
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

str_Respuesta = 'S'
str_Frase = ""
int_Contador = 0

################################################################################

# Inicio del programa:

while str_Respuesta == 'S' or str_Respuesta == 's':

    # SOLICITUD de Datos en PYTHON 2.7
    # str_Frase = raw_input('\nIntroduce una frase: ')

    # SOLICITUD de Datos en PYTHON 3.x
    str_Frase = input('\nIntroduce una frase: ')

    int_Contador = int_Contador + 1

    str_Respuesta = input('Deseas introducir nuevas Frases (S/N):')

print("El numero de frases introducidas es: %d" %(int_Contador))
