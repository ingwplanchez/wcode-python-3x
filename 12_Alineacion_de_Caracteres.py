
# Alineacion de Caracteres

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
#############################################################################

# Declaracion de Constantes

PRODUCTO = 0
DESCRIPCION= 1
CANTIDAD = 2
PRECIO = 3

# Declaracion de variables y colecciones

list_Trama = ['Producto', 'Descripcion', 'Cantidad']
list_Pedido = ['SmartPhone', 'Iphone 12 Pro Max', '2']

list_Trama2 = ['Producto', 'Descripcion', 'Cantidad','Precio']
list_Pedido2 = ['SmartPhone', 'Iphone 12 Pro Max', '2','2000']

str_Centro = " ALINEACION DE CARACTERES "

################################################################################

# Inicio de programa

print("\n" + str_Centro.center(70, "-") + "\n")

print(" Alineado por defecto ".center(70, "*"))

print("{0} | {1} | {2}|"
.format(list_Trama[PRODUCTO],list_Trama[DESCRIPCION],list_Trama[CANTIDAD]))

print("".center(70, "*"))

################################################################################

# Alineado a la izquierda

# '<'    : Alinea a la izquierda, generalmente se omite ya que es la opción
#          por defecto en la mayoría de los objetos.

# {:<X}  : Muestra el contenido alineado a la izquierda y ocupa X caracteres

print("\n")
print(" Alineado a la izquierda ".center(70, "*"))

print("| {:<20} | {:<20} | {:<20} |"
.format(list_Trama[PRODUCTO],list_Trama[DESCRIPCION],list_Trama[CANTIDAD]))

print("".center(70, "*"))

print("| {:<20} | {:<20} | {:<20} |".format(list_Pedido[PRODUCTO]   ,
                                            list_Pedido[DESCRIPCION],
                                            list_Pedido[CANTIDAD]))

################################################################################

# Alineado a la derecha

# '>'    : Alinea a la derecha.
# {:>X}  : Muestra el contenido alineado a la derecha y ocupa X caracteres

print("\n")
print(" Alineado a la Derecha ".center(70, "*"))
print("| {:>20} | {:>20} | {:>20} |"
.format(list_Trama[PRODUCTO],list_Trama[DESCRIPCION],list_Trama[CANTIDAD]))

print("".center(70, "*"))

print("| {:>20} | {:>20} | {:>20} |".format(list_Pedido[PRODUCTO]   ,
                                            list_Pedido[DESCRIPCION],
                                            list_Pedido[CANTIDAD]))

################################################################################

# Centrado del texto

# '^'    : Centrado del texto
# {:^X}  : Muestra el contenido centrado y ocupa X caracteres

print("\n")
print(" Centrado del texto ".center(70, "*"))
print("| {:^20} | {:^20} | {:^20} |"
.format(list_Trama[PRODUCTO],list_Trama[DESCRIPCION],list_Trama[CANTIDAD]))
print("".center(70, "*"))
print("| {:^20} | {:^20} | {:^20} |".format(list_Pedido[PRODUCTO]   ,
                                            list_Pedido[DESCRIPCION],
                                            list_Pedido[CANTIDAD]))

################################################################################

# Ejemplo

##print("\n")
##print(" EJEMPLO ".center(80, "-"))

print("\n")
print("".center(80, "*"))
print("| {:^20} | {:^20} | {:^10} | {:^18}|\n".format(list_Trama2[PRODUCTO],
                                                  list_Trama2[DESCRIPCION],
                                                  list_Trama2[CANTIDAD],
                                                  list_Trama2[PRECIO]))

print("".center(80, "*"))
print("| {:^20} | {:^20} | {:^10} | {:^18}|\n".format(list_Pedido2[PRODUCTO],
                                            list_Pedido2[DESCRIPCION],
                                            list_Pedido2[CANTIDAD],
                                            list_Pedido2[PRECIO]))

################################################################################

