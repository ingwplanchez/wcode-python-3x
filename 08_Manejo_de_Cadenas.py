
# Manejo de Cadenas

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
# list_Nombre_Lista = [dato1,dato2,...] ;   Elementos de una lista

#################################################################################

# Manejo de Listas

# lista[INDICE]                         ;   Dato guardado en el INDICE
# lista = []                            ;   Lista vacia

# Particionado
#
# lista[INICIO:FIN]
# lista[INICIO:FIN:SALTO]
# lista[:]
# Lista[INDICE:]
# Lista[:FIN]
# Lista[::SALTO]

# Metododos de Listas
#
# lista.append(dato)                    ;   Agrega nuevos elementos
# lista.extend([dato1,dato2,...]        ;   Agregar uno a uno nuevos elementos
# len(lista)                            ;   Permite saber el tama?o de una lista
# lista.remove(dato)                    ;   Remueve un elemento que se le pase
#                                           como paramentro de la lista a donde
#                                           se este aplicando.
# lista.pop(indice)                     ;   Remueve un elemento por su indice
# lista.index(elemento)                 ;   Devuelve el n?mero de indice del
#                                           elemento pasado como parametro
# list.count(elemento)                  ;   Se usa para saber las veces que se
#                                           repite un elemento dentro de la lista.
# lista.reverse()                       ;   Permite invertir los elementos  de
#                                           una lista.
#
#################################################################################


## [subcode]

# IDLEx
# Descarga: http://idlex.sourceforge.net/download.html

# Declaracion de constantes

PORT_DB_SERVER =    3307
USER_DB_SERVER =    "root"
PASS_DB_SERVER =    "123456"
DB_NAME        =    "nomina"

# Declaracion de variables

list_Trama = ['Producto', 'Descripcion', 'Cantidad', 'Precio']
list_Lista_Vacia = []
list_Lista_Vacia2 = []
str_Trama = ""
str_Trama2 = ""

#################################################################################

print("\n***********METODOS DE SEPARACION Y UNION***********\n")

print("1) Metodo join()")
str_Trama = " ".join(list_Trama)
str_Trama2 = "|".join(list_Trama)

print("\n- Lista original  : " + str(list_Trama) )
print("\n- Cadena formateada con ' ': " + str_Trama )
print("\n- Cadena formateada con '|': " + str_Trama2 )

#################################################################################

## [subcode]

print("\n2) Metodo split()")

print("\n- split() por defecto con ' ':\n")

print("Cadena Original: "+str_Trama)
list_Lista_Vacia = str_Trama.split()
print("List Final     : "+str(list_Lista_Vacia))

print("\n- split('X') con separador '|':\n")
print("Cadena Original: "+str_Trama2)

list_Lista_Vacia = str_Trama2.split('|')
print("Lista Final    : "+str(list_Lista_Vacia))

################################################################################

## [subcode]

print ("\n*************EXTRACCION DE SUBSTRINGS*************\n")

str_Trama = ""
str_Trama = str(PORT_DB_SERVER)+USER_DB_SERVER+PASS_DB_SERVER+DB_NAME

print("TRAMA  : "+ str_Trama)
print("\nPuerto : " + str_Trama[:4])
print("Usuario: " + str_Trama[4:8])
print("Clave  : " + str_Trama[8:14])
print("Tabla  : " + str_Trama[14:])

#         5C       5C          5E       3E + 2D
# Trama = Producto|Descripcion|Cantidad|Precio
# Trama = ProductoDescripcionCantidadPrecio
