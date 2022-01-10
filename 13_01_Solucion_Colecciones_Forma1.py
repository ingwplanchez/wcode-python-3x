
# FORMA 1

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

ANCHO   = 75
RELLENO = "*"
COMILLAS = ""
MENSAJE = "TOTAL"

# Definicion de Tramas

list_Trama = ["Producto", "Descripcion", "Cantidad", "Precio"]

list_Producto1 = ["2000", "1", "Iphone 12 pro Max", "Smartphone"]
list_Producto2 = ["1500", "1", "Iphone 12 pro Max", "Smartphone"]
list_Producto3 = ["1200", "1", "Iphone 12 pro Max", "Smartphone"]
list_Producto4 = ["1000", "1", "Iphone 12 pro Max", "Smartphone"]

# Formato para mostrar variables: str_Formato.format()

str_Formato = "|{:^20}|{:^20}|{:^15}|{:^15}|"
str_Total   = "|{:^20} {:^20} {:^15}|{:^15}|"

# Variable para almacenar la sumatoria de precios Total

int_Total = 0

################################################################################

# Inicio del Programa

# Se aplica el Metodo .reverse() para ordenar las listas

list_Producto1.reverse()
list_Producto2.reverse()
list_Producto3.reverse()
list_Producto4.reverse()

print (COMILLAS.center(ANCHO,RELLENO))

print(str_Formato.format(list_Trama[PRODUCTO],
                         list_Trama[DESCRIPCION],
                         list_Trama[CANTIDAD],
                         list_Trama[PRECIO]))

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

