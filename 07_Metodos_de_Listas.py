
# Metodos para el manejo de listas Listas

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

# Declaracion de variables

# Posiciones  0      1      2       3     4
list_Lista = ['Hola','Soy','WCode',[1,2] ,3]

list_Lista2 = ['Hola'   ,
               'Soy'    ,
               'WCode'  ,
                2       ,
                3]

list_Lista_vacia = []

print ("\n*********METODOS DE UNA LISTA*********\n")

print("- Lista original:\n")
print(list_Lista)

print("\n- Lista 2:\n")
print(list_Lista2 )

print("\n- Lista vacia:\n")
print(list_Lista_vacia)

print("\n- Lista Modificada:\n")
list_Lista[0] = 'Adios'
print(list_Lista)

#############################################################################

# lista.append(dato): Este método nos permite agregar nuevos
# elementos a una lista.
print("\n1) AGREGAR UN ELEMENTO: lista.append(dato)")
list_Lista.append([4,5,6,7])

print("\n- Nueva Lista:\n")
print(list_Lista)

############################################################################

# lista.extend([dato1,dato2,...]: permite agregar uno a uno
# nuevos elementos

print("\n2) EXTENDER UNA LISTA: lista.extend([dato1,dato2,...])")
list_Lista.extend([4,5,6,7])

print("\n- Nueva Lista:\n")
print(list_Lista)
############################################################################

# len(lista): Muestra la longitud de una lista.

print("\n3) LONGITUD DE UNA LISTA : len(lista)\n")
print("- Longitud de la lista %d" %(len(list_Lista)))

############################################################################

# lista.remove(dato): remueve un elemento que se le pase como
# parámentro de la lista a donde se le esté aplicando.

print("\n4) REMOVER UN ELEMENTO: lista.remove(dato)")
list_Lista.remove(3)

print("\n- Nueva Lista:\n")
print(list_Lista)

############################################################################

# lista.pop(indice): remueve un elemento por su indice

print("\n5) REMOVER POR INDICE: lista.pop(indice)")
list_Lista.pop(1)

print("\n- Nueva Lista:\n")
print(list_Lista)

############################################################################

# lista.index(elemento): devuelve el número de indice del
# elemento que le pasemos por parámetro.

print("\n6) INDEX DE UN ELEMENTO: lista.index(elemento)")
print("\n \'Wcode\' es el indice %d de la lista" %(list_Lista.index('WCode')))

############################################################################

# list.count(elemento): se usa para saber las veces que se repite un elemento
# dentro de la lista.

print("\n7) EXTENDER UNA LISTA: lista.index(elemento)")
print("\n 'Wcode' aparece %d vez en la lista" %(list_Lista.count('WCode')))

############################################################################

# lista.reverse(): Permite invertir los elementos  de una lista.
print("\n8) INVERTIR UNA LISTA: lista.reverse()")
list_Lista.reverse()

print("\n- Nueva Lista:\n")
print(list_Lista)

#############################################################################







