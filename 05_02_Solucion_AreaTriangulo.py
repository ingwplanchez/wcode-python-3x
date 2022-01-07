
# 2) Programa que solicite al usuario los datos para calcular
# el area de un Triangulo.

# VARIABLES

int_Base = 0
int_Altura = 0
float_Area = 0.0

# Incio de programa

print("CALCULAR EL AREA DEL TRIANGULO")

int_Base = int(input('Introduzca el valor de la Base: '))
int_Altura = int(input('Introduzca el valor de la Altura:'))

# AREA DEL TRIANGULO
# Area = (Base*Altura)/2
float_Area = (int_Base*int_Altura)/2

print("El area del triangulo es:  %0.2f"%(float_Area))
