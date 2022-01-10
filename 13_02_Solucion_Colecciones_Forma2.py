
# FORMA 2

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

# Indices de la trama

PRODUCTO = 0
DESCRIPCION = 1
CANTIDAD = 2
PRECIO = 3

# Valores para dibujar la tabla

ANCHO    = 75
RELLENO  = "*"
COMILLAS = ""
MENSAJE  = "TOTAL"
SEPARADOR = "|"

# Definicion de Tramas

tuple_Trama = ('Producto', 'Descripcion', 'Cantidad','Precio')

str_Producto1 = 'Smartphone|Iphone 12 Pro Max|1|2000'
str_Producto2 = 'Smartphone|Iphone 11 Pro Max|1|1500'
str_Producto3 = 'Smartphone|Iphone 10 Pro Max|1|1200'
str_Producto4 = 'Smartphone|Iphone 09 Pro Max|1|1000'

# Formato para mostrar variables: str_Formato.format()

str_Formato = "|{:^20}|{:^20}|{:^15}|{:^15}|"
str_Total   = "|{:^20} {:^20} {:^15}|{:^15}|"

# Declaracion de Listas Vacias para guardar los elementos de str_Producto

list_Producto1 = []
list_Producto2 = []
list_Producto3 = []
list_Producto4 = []

# Variable para almacenar la sumatoria de precios Total

int_Total = 0

################################################################################

# Inicio del Programa

# Se aplica el metodo .split() y se guardan los elementos en una lista

list_Producto1 = str_Producto1.split(SEPARADOR)
list_Producto2 = str_Producto2.split(SEPARADOR)
list_Producto3 = str_Producto3.split(SEPARADOR)
list_Producto4 = str_Producto4.split(SEPARADOR)

print (COMILLAS.center(ANCHO,RELLENO))

print(str_Formato.format(tuple_Trama[PRODUCTO],
                         tuple_Trama[DESCRIPCION],
                         tuple_Trama[CANTIDAD],
                         tuple_Trama[PRECIO]))

print (COMILLAS.center(ANCHO,RELLENO))

print(str_Formato.format(list_Producto1[PRODUCTO],
                         list_Producto1[DESCRIPCION],
                         list_Producto1[CANTIDAD],
                         list_Producto1[PRECIO]))

print(str_Formato.format(list_Producto2[PRODUCTO],
                         list_Producto2[DESCRIPCION],
                         list_Producto2[CANTIDAD],
                         list_Producto2[PRECIO]))

print(str_Formato.format(list_Producto3[PRODUCTO],
                         list_Producto3[DESCRIPCION],
                         list_Producto3[CANTIDAD],
                         list_Producto3[PRECIO]))

print(str_Formato.format(list_Producto4[PRODUCTO],
                         list_Producto4[DESCRIPCION],
                         list_Producto4[CANTIDAD],
                         list_Producto4[PRECIO]))

print (COMILLAS.center(ANCHO,RELLENO))

int_Total= int (list_Producto1[PRECIO])+int (list_Producto2[PRECIO])+int (list_Producto3[PRECIO])+int (list_Producto4[PRECIO])

print(str_Total.format(COMILLAS,COMILLAS,MENSAJE,int_Total))

print (COMILLAS.center(ANCHO,RELLENO))






