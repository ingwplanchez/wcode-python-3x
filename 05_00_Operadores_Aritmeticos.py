
# Operadores Aritméticos

# ESTILO WCODE

# Variables
# int_Nombre_variable = tipo_dato       ;   Variables del tipo entero  
# float_Nombre_variable = tipo_dato     ;   Variables con decimales       
# str_Nombre_variable = tipo_dato       ;   variables con Cadenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   variables booleanas

# Constantes
# const_NOMBRE_CONSTANTE = tipo_dato    ;   constante de cualquier tipo de datos

# Principales operadores aritméticos en Python

# Símbolo        Significado         Ejemplo         Resultado
# +              Suma                a = 10 + 5      a es 15
# -              Resta               a = 12 - 7      a es 5
# *              Multiplicación      a = 7 * 5       a es 35
# **             Exponente           a = 2 ** 3      a es 8
# /              División            a = 12.5 / 2    a es 6.25
# //             División entera     a = 12.5 // 2   a es 6.0
# %              Módulo              a = 7 % 2       a es 1

# Formato Moneda
# Trama = 6E.3D

#Declaracion de Variables

str_Trama = "2500000777" # 6E+3D = 2500000.777
int_Parte_Entera = 0     # 6E
int_Parte_Decimal = 0    # 3D
 
#Programa principal 

print("******FORMATEAR TRAMA*******")
print("")
print("****************************")
print("Trama inicial: %s"%(str_Trama))
print("****************************")
print("")

int_Parte_Entera = int(str_Trama)/1000
print("Parte Entera  (6E): %d " %(int_Parte_Entera ))
int_Parte_Decimal = int(str_Trama) % 1000
print("Parte Decimal (3D): %d " %(int_Parte_Decimal))
print("")

print("****************************")
print("Precio(6E+3D): %d.%d" %(int_Parte_Entera,int_Parte_Decimal))
print("****************************")

###############################################################################################

#EJERCICIOS (Mostrar el resultado en pantalla)

# 1) Programa que solicite al usuario los datos para calcular el area de un Cuadrado 
# 2) Programa que solicite al usuario los datos para calcular el area de un Triangulo
# 3) Programa que solicite al usuario los datos para calcular el area de un Circulo
# 4) Programa que solicite al usuario los datos para llevar Grados farenheit a Grados Celcius
# 5) Sumar 4 Tramas de datos(Stings) que contengan el precio de un producto.

#    Consideraciones:

#    Trama = 6E + 3D
#    La suma no debe exceder el numero 999999999

# FORMULAS

# AREA DEL CUADRADO
# A = Lado ** 2

# AREA DEL TRIANGULO
# A = (Base*Altura)/2

# AREA DE UN CIRCULO
# A = PI*(Radio**2)

# FAHRENHEIT A CELCIUS
# celcius = (fahrenheit - 32.0) * 5.0 / 9.0









