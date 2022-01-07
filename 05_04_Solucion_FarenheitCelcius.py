
# 4) Programa que solicite al usuario los datos para llevar
# Grados farenheit a Grados Celcius

# VARIABLES

int_farenheit = 0
float_celcius = 0.0

# Incio de programa

print("LLEVAR GRADOS FARENHEIT A CELCIUS")

int_farenheit = int(input('Introduzca los grados Farenheit: '))

# FAHRENHEIT A CELCIUS
# celcius = (fahrenheit - 32.0) * 5.0 / 9.0
float_celcius = (int_farenheit-32.0)*5.0/9.0

print("Grados Celsius:  %0.2f"%(float_celcius))

