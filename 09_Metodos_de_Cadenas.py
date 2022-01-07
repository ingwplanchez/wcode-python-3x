
# Metodos para el manejo de cadenas

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


#############################################################################

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
#############################################################################

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
#############################################################################

## [subcode]

print("\n******************METODOS DE ANALISIS********************\n")

# cadena.count():   retorna el numero de veces que se repite un conjunto
#                   de caracteres especificado.

str_cadena = ""
print("1) Metodo count():")

str_cadena = "Hola WCODE"
str_cadena.count("Hola")

print("- La palabra 'Hola' aparece %d vez" %(str_cadena.count("Hola")))

#############################################################################

## [subcode]

# cadena.find()  : Retornan la ubicacion en la que se encuentra el argumento
#                  indicado.

print("\n2) Metodo find():\n")
print("- Indice Encontrado: %d " %(str_cadena.find("WCODE")))
print("- Indice fallido   : %d " %(str_cadena.find("Mundo")))

#############################################################################

## [subcode]

# cadena.index() : Retorna la ubicacion en la que se encuentra el argumento
#                  indicado

print("\n3) Metodo index():\n")
print("- Indice encontrado: %d " %(str_cadena.index("WCODE")))
##print("- Indice fallido   : %d " %(str_cadena.index("Mundo")))

#############################################################################

## [subcode]

# cadena.startswith("Subcadena"): Permite Saber si una cadena comienza con una
#                                 subcadena determinada.

# cadena.endswith("Subcadena")  : Permite Saber si una cadena finaliza con una
#                                 subcadena determinada.

# STX: Inicio de la Trama (02)
# ETX: Fin de la trama    (03)

# Trama = STX|DATOS|ETX

str_Trama1 = '02|Producto|Descripcion|Cantidad|Precio|03'
str_Trama2 = '00|Producto|Descripcion|Cantidad|Precio|00'

print("\n4) Metodo startswith()  :\n")
print("- Inicio de Trama 1 (02): %s" %(str_Trama1.startswith("02") ))
print("- Inicio de Trama 2 (02): %s \n" %(str_Trama2.startswith("02") ))

print("5) Metodo endswith()   :\n")
print("- Fin de Trama 1   (03): %s" %(str_Trama1.endswith("03") ))
print("- Fin de Trama 2   (03): %s" %(str_Trama2.endswith("03") ))

#############################################################################

## [subcode]

print("\n******************METODOS DE VALIDACION********************\n")

# Cadena.isdigit() : Permite saber si una cadena es num?rica
# Cadena.isalnum() : Permite saber si una cadena es alfanum?ricas
# Cadena.isalpha() : Permite saber si una cadena es alfab?tica
# Cadena.isspace() : Permite saber si una cadena contiene solo espacios
#                    en blanco

str_Cadena = "123456"
print ("6) Metodo isdigit():\n")
print("- La cadena '%9s' es Numerica?        | %s\n" %(str_Cadena,str_Cadena.isdigit()))

str_Cadena = "WCODE123"
print ("7) Metodo isalnum():\n")
print("- La cadena '%9s' es Alfanumerica?    | %s\n" %(str_Cadena,str_Cadena.isalnum()))

str_Cadena = "HolaWCODE"
print ("8) Metodo isalpha():\n")
print("- La cadena '%9s' es Alfabetica?      | %s\n" %(str_Cadena,str_Cadena.isalpha()))

str_Cadena = " "
print ("9) Metodo isspace():\n")
print("- La cadena '%9s' contiene espacios?  | %s" %(str_Cadena,str_Cadena.isspace()))

#############################################################################

## [subcode]

print("\n*****************METODOS DE TRANSFORMACION*****************\n")

# cadena.upper() : Permite Convertir una cadena a may?sculas
# cadena.lower() : Permite Convertir una cadena a min?sculas
# cadena.replace("Cadena","Nuevacadena") : Permite reemplazar una cadena
#                                          por otras

str_Cadena = "De 0 a ProGramaDor"

print ("10) Metodo upper():\n")
print("- Cadena Original      : %s" %(str_Cadena))
print("- Cadena en mayusculas : %s\n" %(str_Cadena.upper()))

print ("11) Metodo lower():\n")
print("- Cadena Original      : %s" %(str_Cadena))
print("- Cadena en Minusculas : %s\n" %(str_Cadena.lower()))

print ("12) Metodo replace(Cadena,Nuevacadena):\n")
print("- Cadena Original      : %s" %(str_Cadena))
print("- Cadena reemplazada   : %s\n" %(str_Cadena.replace("ProGramaDor", "Profesional")))

## [subcode]

# cadena.center(Longitud,Caracter_relleno): Devuelve una  cadena centrada
# cadena.ljust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           Izquierda
# cadena.rjust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           derecha

str_Izquierda = "TEXTO ALINEADO A LA IZQUIERDA "
str_Centro = " TEXTO ALINEADO AL CENTRO "
str_Derecha = " TEXTO ALINEADO A LA DERECHA"

str_Tabla = """\
+---------------------------------------------------------------------+
| WCODE:                  SI LO IMAGINAS LO CREAS                     |
|---------------------------------------------------------------------|
|                        CURSO DE 0 A PROGRAMADOR!                    |
+---------------------------------------------------------------------+
"""\

print("\n" + str_Izquierda.ljust(71, "*"))
print("\n" + str_Centro.center(71, "*"))
print("\n" + str_Derecha.rjust(71, "*"))

print("\n" + str_Tabla + "\n")

## [subcode]
