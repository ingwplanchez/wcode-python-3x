
#Estructuras Alternativas.

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

# OPERADORES ARITMÉTICOS

# ---------------------------------------------------------------------------
# Símbolo        Significado         Ejemplo         Resultado

# +              Suma                a = 10 + 5      a es 15
# -              Resta               a = 12 - 7      a es 5
# *              Multiplicación      a = 7 * 5       a es 35
# **             Exponente           a = 2 ** 3      a es 8
# /              División            a = 12.5 / 2    a es 6.25
# //             División entera     a = 12.5 // 2   a es 6.0
# %              Módulo              a = 7 % 2       a es 1

#############################################################################

# OPERADORES CONDICIONALES O DE COMPARACION

# ---------------------------------------------------------------------------
# Símbolo          Significado         Ejemplo         Resultado

# ==               Igual que           5 == 7          Falso
# !=               Distinto que        rojo != verde   Verdadero
# <                Menor que           8 < 12          Verdadero
# >                Mayor que           12 > 7          Falso
# <=               Menor o igual que   12 <= 12        Verdadero
# >=               Mayor o igual que   4 >= 5          Falso

#############################################################################

# OPERADORES LOGICOS

# ---------------------------------------------------------------------------

# Operador        Ejemplo              Resultado
#
# and (y)         5 == 7 and 7 < 12    0 y 0 Falso
#				  9 < 12 and 12 > 7    1 y 1 Verdadero
#                 9 < 12 and 12 > 15   1 y 0 Falso
# or (o)          12 == 12 or 15 < 7   1 o 0 Verdadero

#############################################################################

# Pseudocodigo:

# 1) Instruccion IF:

# 	IF condicion
#		instrucciones
# 	FIN del IF

# Ejemplo:

str_Cadena = 'WCODE'

print ("\n1) if str_Cadena == 'WCODE': ")

if str_Cadena == 'WCODE':
    print ("La condicion es VERDADERA!\n"),

print("\n2) if str_Cadena == 'wcode': ")

if str_Cadena == 'wcode':
    print("La condicon es FALSA!\n")

print("No se ejecuto la condicion\n")

print("3) if str_Cadena != 'wcode':")

if str_Cadena != 'wcode':
    print ("La condicion es VERDADERA!")

#############################################################################

# Pseudocodigo:

# 2) Instruccion IF - ELSE (Una Condicion)

#	IF condicion
#		instrucciones1
#	ELSE
#       instrucciones2
# 	FIN del IF

# Ejemplo:

print("\n4) if str_Cadena == 'wcode' | else: "),

if str_Cadena == 'wcode':
    print ("La condicion es VERDADERA!\n"),

else:
    print("La condicon es FALSA!")

#############################################################################

# Pseudocodigo:

# 3) Instruccion IF - ELSE  (Multiples condiciones)

#	IF condicion1 Operador-Logico1 condicion2
#		instrucciones1
#	ELSE
#       instrucciones2
# 	FIN del IF

# Ejemplo:

print("\n5) if str_Cadena == 'wcode' or str_Cadena == 'WCODE': "),

if str_Cadena == 'wcode' and str_Cadena == 'WCODE':
    print ("La condicion es VERDADERA!\n"),

else:
    print("La condicon es FALSA!")

#############################################################################

# Pseudocodigo:

# ) Instruccion ELSE_IF

#	IF condicion1
#		instrucciones1
#	ELSE_IF condicion2
#       instrucciones2
#	ELSE
#       instrucciones3
# 	FIN del IF

# Ejemplo:

print("\n6) if str_Cadena == 'wcode' | elif str_Cadena == 'WCODE': "),

if str_Cadena == 'WCODE':
    print ("La condicion1 es VERDADERA!\n"),

if str_Cadena == 'WCODE':
    print ("Elif condicion2 VERDADERA!\n"),

else:
    print("La condicon es FALSA!\n")

#############################################################################




