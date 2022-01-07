
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
##    contador = 1
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

bool_Bandera = 0
int_Contador = 1

################################################################################

# Inicio del programa:

while int_Contador <= 10:

    if bool_Bandera == 0:

        print(int_Contador,"Hola")
        bool_Bandera = 1

    else:

        print(int_Contador,"Adios")
        bool_Bandera = 0

    int_Contador = int_Contador + 1
