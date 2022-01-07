
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

## Pseudocodigo:

##    Hacer_1 mientras condicion1
##
##        Hacer_2 mientras condicion2
##
##            Hacer_3 mientras condicion3
##
##            Fin del Hacer_3
##
##         Fin del Hacer_2
##
##    Fin del Hacer_1

################################################################################

## ENUNCIADO 1:

##  Imprimir diez veces la serie de numeros del 1 al 10. Los numeros deben
## aparecer cada 1 segundo

################################################################################

## Estudio previo:
##
##    La secuencia de numeros del 1 al 10 se realiza mediante un ciclo que
##    vaya del 1 al 10 y un contador para generarlos.
##
##    Esta secuencia se debe realizar 10 veces por lo tanto se requiere otro
##    ciclo que cuente las veces que se ha impreso el bucle interno. Este ciclo
##    aumentará en una unidad cuando se hayan visualizado los numeros
##    del 1 al 10.

##    El bucle exterior controla que se imprima 10 veces el bucle interno.


################################################################################

## Variables

##  numero = contador interno para generar los numeros del 1 al 10
##  serie = contador de series externo del 1 al 10

#   Pseudocodigo:

##    numero = 0
##    serie = 1
##
##    Hacer_1 mientras serie <= 10
##
##        numero = 1
##
##        Hacer_2 mientras numero <= 10
##            imprime numero
##            numero = numero + 1
##            espera(1)
##        Fin del Hacer_2
##
##        serie = serie  + 1
##
##    Fin del Hacer_1
##    Fin del programa


################################################################################

import time

# Declaracion de variables:

int_Numero = 0
int_Serie = 1

################################################################################

# Inicio del programa:

print("\nSerie numero: %d \n")%(int_Serie)

while int_Serie <= 10:

    int_Numero = 1

    while int_Numero <= 10:
        print(int_Numero)
        int_Numero = int_Numero + 1
        time.sleep(1)

    int_Serie = int_Serie + 1

    if int_Serie <= 10:
        print("\nSerie numero: %d \n")%(int_Serie)

################################################################################

## ENUNCIADO 2:

##    Hacer un pseudocodigo que simule el funcionamiento de un reloj Digital
##    y que permita ponerle la hora

################################################################################

## Estudio previo:
##
##    Necesitamos 3 ciclos: para las horas, los minutos y los segundos,
##    uno dentro del otro.
##
##    El ciclo mas pequeño será el mas interno y será el primero en terminar.
##
##    Cuando termine aumentaran los minutos; los segundos se inicializan en 0.
##
##    Los minutos al llegar a 60 tendran que pasar a valer 0 y se incrementa
##    la hora
##
##    Al cumplir las 24 horas inicia un nuevo dia. Se puede usar un bucle
##    infinito externo a las horas para que el reloj no se detenga.

##    Formato de presentacion
##
##    HH : MM : SS
##    00 : 00 : 00
##
##    En Python se Utiliza el metodo zfill(n) para hacer que una cadena
##    ocupe n posiciones, añadiendo tantos ceros a la izquierda como sea
##    necesario.
##
##    Ejemplo:
##
##    >>> '23'.zfill(4)
##    '0023'
##
##    >>> str(23).zfill(4)
##    '0023'

################################################################################

## Variables

##    horas = contador de las horas.
##    minutos = contador para los minutos
##    segundos = contador para los segundos
##

#   Pseudocodigo:

##    horas =  0
##    minutos = 0
##    segundos = 0
##
##    imprime "Introduce horas: "
##    introduce horas
##
##    imprime "Introduce minutos: "
##    introduce minutos
##
##    imprime "Introduce segundos: "
##    introduce segundos
##
##    Hacer_1 Mientras TRUE
##        Hacer_2 Mientras horas < 24
##            Hacer_3 Mientras minutos < 60
##                Hacer_4 Mientras segundos < 60
##                    imprime "horas : minutos : segundos"
##                    segundos = segundos + 1
##                    espera(1)
##                fin del Hacer_4
##                minutos = minutos + 1
##                segundos = 0
##            fin del Hacer_3
##            horas = horas + 1
##            minutos = 0
##        fin del Hacer_2
##        horas = 0
##   fin del Hacer_1
##
################################################################################

# Declaracion de variables:


################################################################################

# Inicio del programa: