
# Tuplas y Diccionarios

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

# Metodos de cadenas

# cadena.count():  Retorna el numero de veces que se repite un conjunto 
#                  de caracteres especificado.
# cadena.find()  : Retorna la ubicacion en la que se encuentra el argumento
#                  indicado.
# cadena.index() : Retorna la ubicacion en la que se encuentra el argumento
#                  indicado.
#
# cadena.startswith("Subcadena"): permite Saber si una cadena comienza con una
#                                 subcadena determinada.

# cadena.endswith("Subcadena")  : permite Saber si una cadena finaliza con una
#                                 subcadena determinada.
# 
# Cadena.isdigit() : permite saber si una cadena es numérica
# Cadena.isalnum() : permite saber si una cadena es alfanuméricas
# Cadena.isalpha() : permite saber si una cadena es alfabética
# Cadena.isspace() : permite saber si una cadena contiene solo espacios
#                    en blanco
#
# cadena.upper()   : permite Convertir una cadena a mayúsculas
# cadena.lower()   : permite Convertir una cadena a minúsculas
# cadena.replace("Cadena","Nuevacadena") : permite reemplazar una cadena
#                                          por otras
#
# cadena.center(Longitud,Caracter_relleno): Devuelve una  cadena centrada
# cadena.ljust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           Izquierda  
# cadena.rjust(Longitud,Caracter_relleno):  Devuelve una  cadena alineada a la
#                                           derecha   
#
#############################################################################

## [subcode]

# Declaracion de constantes

# IP_BD_SERVER   =  "127.0.0.1"
# USER_DB_SERVER =  "root"
# PASS_DB_SERVER =  "qwerty"
# DB_NAME        =  "nomina"

IP_BD_SERVER   = 0
USER_DB_SERVER = 1
PASS_DB_SERVER = 2
DB_NAME        = 3

FTP = 'ftp'
SSH = 'ssh'
SMTP = 'smtp'
HTTP = 'http'

str_Centro = " TUPLAS Y CONSTANTES "
print("\n" + str_Centro.center(70, "*") + "\n")

tuple_Conexion_bd = ("127.0.0.1","root","qwerty","nomina")

print ("Conexion tipica:" + str(tuple_Conexion_bd) + "\n")
 
print ("[+] IP    BD    : " + str(tuple_Conexion_bd[IP_BD_SERVER]))
print ("[+] User  BD    : " + str(tuple_Conexion_bd[USER_DB_SERVER]))
print ("[+] Pass  BD    : " + str(tuple_Conexion_bd[PASS_DB_SERVER]))
print ("[+] Table BD    : " + str(tuple_Conexion_bd[DB_NAME]))

#############################################################################

## [subcode]

# diccionario.keys() : Regresa lista de todas las claves en el diccionario
# diccionario.items(): Regresa una lista completa de elementos del diccionario

str_Centro = " MANEJO DE DICCIONARIOS "
print("\n" + str_Centro.center(70, "*") + "\n")

dic_Services = {'ftp':21,'ssh':22,'smtp':25,'http':80}

print("LLaves del diccionario: ")
print(str(dic_Services.keys()) + "\n")

print("Elementos del diccionario: ")
print(str(dic_Services.items())  + "\n")

print("[+] Valor %4s encontrado en el puerto %d" %(FTP.upper(),dic_Services[FTP]))
print("[+] Valor %4s encontrado en el puerto %d" %(SSH.upper(),dic_Services[SSH]))
print("[+] Valor %4s encontrado en el puerto %d" %(SMTP.upper(),dic_Services[SMTP]))
print("[+] Valor %4s encontrado en el puerto %d" %(HTTP.upper(),dic_Services[HTTP]))

#############################################################################

## [subcode]

