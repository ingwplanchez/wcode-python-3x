
# Ejercicios de Colecciones y cadenas

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
#                                           como par?mentro de la lista a donde
#                                           se est? aplicando.
# lista.pop(indice)                     ;   Remueve un elemento por su indice
# lista.index(elemento)                 ;   Devuelve el n?mero de indice del
#                                           elemento pasado como par?metro
# list.count(elemento)                  ;   Se usa para saber las veces que se
#                                           repite un elemento dentro de la lista.
# lista.reverse()                       ;   Permite invertir los elementos  de
#                                           una lista.
#
################################################################################

# Manejo de Cadenas

# Datos dentro de una cadena
# %d                                    ;   Numero entero dentro de la cadena
# %f                                    ;   Numero Flotante Dentro de la cadena
# %s                                    ;   String dentro de la cadena

# Formateo de datos
# str(lista)                            ;   Lista Formateada como String
# str(Numero)                           ;   Dato Numerico formateado como string
# int(Cadena)                           ;   Cadena numerica formateada como Entero
# float(Cadena)                         ;   Cadena numerica Formateada como float

# Metodos de listas
#
# "X".join(lista)                       ;   Une los elementos de una lista donde
#                                       ;   "X" es el simbolo usado para la union
#                                       ;   de los elementos

# Cadena.split('X')                     ;   Separa los elementos de la cadena
#                                       ;   Cada vez que el interprete consiga
#                                       ;   El elemento separador X

# Substrings
# cadena[:FIN]
# cadena[INICIO:FIN]
# cadena[INDICE:]
#

################################################################################

# Metodos de cadenas

# cadena.count():   retorna el numero de veces que se repite un conjunto
#                   de caracteres especificado.

# cadena.find()  : Retornan la ubicacion en la que se encuentra el argumento
#                  indicado.

# cadena.index() : Retorna la ubicacion en la que se encuentra el argumento
#                  indicado.

# cadena.startswith("Subcadena"): Permite Saber si una cadena comienza con una
#                                 subcadena determinada.

# cadena.endswith("Subcadena")  : Permite Saber si una cadena finaliza con una
#                                 subcadena determinada.

# Cadena.isdigit() : Permite saber si una cadena es numerica
# Cadena.isalnum() : Permite saber si una cadena es alfanumericas
# Cadena.isalpha() : Permite saber si una cadena es alfabetica
# Cadena.isspace() : Permite saber si una cadena contiene solo espacios
#                    en blanco

# cadena.upper() : Permite Convertir una cadena a mayusculas
# cadena.lower() : Permite Convertir una cadena a minusculas

# cadena.replace("Cadena","Nuevacadena") : Permite reemplazar una cadena
#                                          por otras

# cadena.center(Longitud,Caracter_relleno): Devuelve una  cadena centrada

# cadena.ljust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           Izquierda.

# cadena.rjust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           derecha.
#
################################################################################

PRODUCTO = 0
DESCRIPCION = 1
CANTIDAD = 2
PRECIO = 3

# Declaracion de variables y colecciones

list_Trama = ['Producto', 'Descripcion', 'Cantidad','Precio']

# FORMA 1

list_Producto1 = ['2000','1', 'Iphone 12 Pro Max','Smartphone']
list_Producto2 = ['1500','1', 'Iphone 11 Pro Max','Smartphone']
list_Producto3 = ['1200','1', 'Iphone 10 Pro Max','Smartphone']
list_Producto4 = ['1000','1', 'Iphone 09 Pro Max','Smartphone']

# FORMA 2

## tuple_Trama = ('Producto', 'Descripcion', 'Cantidad','Precio')

## str_Producto = 'Smartphone|Iphone 12 Pro Max|1|2000'
## str_Producto = 'Smartphone|Iphone 11 Pro Max|1|1500'
## str_Producto = 'Smartphone|Iphone 10 Pro Max|1|1200'
## str_Producto = 'Smartphone|Iphone 09 Pro Max|1|1000'

# Resultado final

## *****************************************************************************
## |       Producto       |     Descripcion      |  Cantidad   |      Precio   |
## *****************************************************************************
## |      SmartPhone      |  Iphone 12 Pro Max   |      1      |       2000    |
## |      SmartPhone      |  Iphone 11 Pro Max   |      1      |       1500    |
## |      SmartPhone      |  Iphone 10 Pro Max   |      1      |       1200    |
## |      SmartPhone      |  Iphone 09 Pro Max   |      1      |       1000    |
## *****************************************************************************
## |                                                  TOTAL    |       5700    |
## *****************************************************************************

