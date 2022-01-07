
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

# Importación de módulos en Python

import time

################################################################################

# Declaracion de variables:

horas    = 0
minutos  = 0
segundos = 0

################################################################################

# Inicio del programa:

# SOLICITUD de Datos en PYTHON 2.7
##horas    = int(raw_input('\nIntroduce horas: '))
##minutos  = int(raw_input('\nIntroduce minutos: '))
##segundos = int(raw_input('\nIntroduce segundos: '))

# SOLICITUD de Datos en PYTHON 3.x
horas    = int(input('Introduce horas: '))
minutos  = int(input('Introduce minutos: '))
segundos = int(input('Introduce segundos: '))

print("")
print("%02d:%02d:%02d" %(horas,minutos,segundos))

# Hacer_1 Mientras TRUE
while True:

    # Hacer_2 Mientras horas < 24
    while horas < 24:
        # Hacer_3 Mientras minutos < 60
        while minutos < 60:
            # Hacer_4 Mientras segundos < 60
            while segundos <60:
                print("%02d:%02d:%02d" %(horas,minutos,segundos))
                segundos = segundos + 1
                time.sleep(1)
            # fin del Hacer_4
            minutos = minutos + 1
            segundos = 0
        # fin del Hacer_3
        horas = horas + 1
        minutos = 0
    # fin del Hacer_2
    horas = 0
# fin del Hacer_1

