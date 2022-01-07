
# 5) Sumar 4 Tramas de datos(Stings) que contengan el precio de un producto.

#    Consideraciones:

#    Trama = 6E + 3D
#    Representacion = 6E.3D
#    La suma no debe exceder el numero 999999999

# VARIABLES

# Se definen 4 variables del tipo String manualmente

str_Precio1 = "11111111"
str_Precio2 = "22222222"
str_Precio3 = "33333333"
str_Precio4 = "44444444"

# Inicializacion de Variables

int_Total = 0
int_Parte_Entera = 0
int_Parte_Decimal = 0

#  Se Transforma cada valor a un entero y se suma en una variable

int_Total = int(str_Precio1) + int(str_Precio2) + int(str_Precio3) + int(str_Precio4)

# Se Calcula la parte entera y la parte decimal: (6E+3D)

print("****************************")

int_Parte_Entera = int_Total / 1000
print("Parte Entera  (6E): %d " %(int_Parte_Entera ))

int_Parte_Decimal = int_Total % 1000
print("Parte Decimal (3D): %d " %(int_Parte_Decimal))

# Se muestra un mensaje con los valores en pantalla

print("****************************")
print("Precio(6E+3D): %d.%03d" %(int_Parte_Entera,int_Parte_Decimal))
print("****************************")

