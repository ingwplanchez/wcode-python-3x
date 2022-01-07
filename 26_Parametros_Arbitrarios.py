
# Funciones con parametros arbitrarrios

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

# Declaracion de variables

# x  = 1
# y  = 2
# z  = 3

x,y,z = 1,2,3

seccion = 1
nombres = ['Juan', 'Antonio', 'Pedro', 'Herminio']
asignaturas = {'matematica': 20, 'fisica': 19, 'quimica': 18}

################################################################################

# Declaracion de funciones

def funcion(x,y,z):
    print("\nParametros de la funcion: \n x = %d, y = %d, z = %d" %(x,y,z))

def alumnos(*lista):

    print("\nLISTA DE ALUMNOS\n")

    for nombre in lista:
        print(nombre)


def notas(seccion, *lista , **asignaturas):

    print("\nALUMNOS EN LA SECCION: %d\n" %(seccion))

    for nombre in lista:
        print(nombre.upper()+"\n")

        for elemento in asignaturas.items():
            print(elemento)

        print("\n")

################################################################################

# Inicio del programa:

funcion(x,y,z)

alumnos(*nombres)

notas(seccion, *nombres, **asignaturas)
