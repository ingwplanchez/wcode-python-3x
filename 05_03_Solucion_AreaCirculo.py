
# 3) Programa que solicite al usuario los datos para calcular
# el area de un Circulo


# CONSTANTES

PI = 3.1416 # Valor aproximado de PI

# VARIABLES

int_Radio  = 0
float_Area = 0

# Incio de programa

print("CALCULAR EL AREA DEL CIRCULO")

int_Radio = int(input('Introduzca el radio del circulo: '))

# AREA DE UN CIRCULO
# Area = PI*(Radio**2)
float_Area = PI*(int_Radio**2)

print("El area del circulo es:  %0.2f"%(float_Area))