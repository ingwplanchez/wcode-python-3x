
# Arrays (Listas)

# ESTILO WCODE

# Variables
# int_Nombre_variable = tipo_dato       ;   Variables del tipo entero
# float_Nombre_variable = tipo_dato     ;   Variables con decimales
# str_Nombre_variable = tipo_dato       ;   variables con Cadenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   variables booleanas

# Constantes
# const_NOMBRE_CONSTANTE = tipo_dato    ;   constante de cualquier tipo de datos
# NOMBRE_CONSTANTE = tipo_dato

# Colecciones
# list_Nombre_Lista = [dato1,dato2,...]

# Declaracion de Constantes

INICIO =  0
FIN = -1
INDICE = 2
SALTO = 1

# Declaracion de variables

# Index:       0     1      2       3     4
list_Lista = ["Hola",'Soy','WCode',[1,2] ,3]


###################################################################################

print ("\n********ELEMENTOS DE LA LISTA********\n")

print (list_Lista[0])       # Hola
print (list_Lista[1])       # Soy
print (list_Lista[2])       # WCode
print (list_Lista[3])       # [1,2]
print (list_Lista[3][0])    # 1
print (list_Lista[3][1])    # 2
print (list_Lista[-1])      # 3
print (list_Lista[-2])      # [1,2]

###################################################################################

print("\n*********FORMATEAR ELEMENTOS**********\n")

print("Las cadenas son: "+list_Lista[0]+" "+list_Lista[1]+" "+list_Lista[2])

print("Elementos Formateados: "+str(list_Lista[3])+" y "+str(list_Lista[4]))

###################################################################################

print ("\n***********NUMEROS MAGICOS************\n")
print("Posicion inicial: " + str(INICIO)+ "\n")
print (list_Lista[INICIO]) # Hola

print("\nPosicion final: " + str(FIN) + "\n")
print (list_Lista[FIN])     # 3

#################################################################################

print ("\n*******PARTICIONADO DE LISTAS*********\n")
print("Imprimir listas:\n")
print (list_Lista)

# lista(inicio:fin)
#Se omite el elemento "fin"
print("\nParticionado: lista(inicio:fin)\n")
print (list_Lista[0:4])
print (list_Lista[0:])

# lista(inicio:fin:salto)
print("\nParticionado: lista(inicio:fin:salto)")
print("Numero      : lista(0:2:1)\n")
print (list_Lista[0:2:1])

print("\nParticionado: lista(inicio:fin:salto)")
print("Constantes  : lista(INICIO:INDICE:SALTO)\n")
print (list_Lista[INICIO:INDICE:SALTO])

################################################################################

print ("\n*******PARTICIONADO POR DEFECTO*********\n")

print("Imprime todos los elementos:")
print (list_Lista[:])

print("\nImprime desde el indice 2 incluyendo e ultimo:")
print (list_Lista[2:])  # print (list_Lista[INDICE:])

print("\nImprime un rango:")
print (list_Lista[:4])  # print (list_Lista[:FIN])

print("\nMuestra los datos de 1 en 1:")
print (list_Lista[::1]) # print (list_Lista[::SALTO])

print("\nMuestra los Datos de 2 en 2:")
print (list_Lista[::2]) # print (list_Lista[::SALTO])














