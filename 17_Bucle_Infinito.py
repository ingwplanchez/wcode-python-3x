
# Bucle infinito

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

# Usos especiales de las variables

# Contadores
# Variable  = Variable +/- CONSTANTE

# Acumuladores o Sumadores
# Acumulador = Acumulador +/- Variable)

#############################################################################

# Pseudocodigo:

# Instruccion WHILE:

# 	HACER MIENTRAS condicion
#		instrucciones
# 	FIN del HACER

# Ejemplo:

# Declaracion de variables

int_Intentos = 0
str_Clave = "ABC123"
str_Cadena = " BUCLE INFINITO "

print("\n" + str_Cadena.center(35, "*") + "\n")

while True:

    str_Password = input("Indique la clave: ")

    # Contador
    int_Intentos = int_Intentos  + 1

    if str_Password == str_Clave :
        print("Clave Correcta!\n")
        int_Intentos = 0

    elif int_Intentos == 3:
        print("Usuario Bloqueado\n")
        break

    else:
        print("Clave incorrecta intento: {} \n".format(int_Intentos))

print("".center(35, "*"))


