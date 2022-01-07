#Introducir datos

# ESTILO WCODE

# int_Nombre_variable = tipo_dato       ;   Variables del tipo entero  
# float_Nombre_variable = tipo_dato     ;   Variables con decimales       
# string_Nombre_variable = tipo_dato    ;   variables con Cadenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   variables booleanas

# Pseudocódigo:

# nombre_variable = tipo_dato
# introducir nombre_variable
# imprime “comentario”

#Declaracion de variables

int_Edad = 0
float_Estatura = 0.0
str_Inicial = ""
str_Apellido = ""

#Inicio del programa

int_Edad = int(input('Introduce tu edad: '))
float_Estatura = float(input('Introduce Tu estatura: '))
str_Inicial = input('Introduce la inicial de tu nombre: ')
str_Apellido = input('Introduce Tu apellido: ')

print ("")
print ("TUS DATOS SON:")
print ("")
print ("Tu Edad es:        %d" %(int_Edad ))
print ("Tu Estatura :      %1.2f" %(float_Estatura))
print ("Tu Inicial:        %s" %(str_Inicial))
print ("Tu Apellido:       %s" %(str_Apellido))

