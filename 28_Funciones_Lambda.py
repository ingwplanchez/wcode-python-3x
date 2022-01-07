
# Funciones lambda

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
################################################################################

## Pseudocodigo:

#  variable = lambda parametro1, parametro2 : expresion

#  Ejemplo:
#  num = lambda x,y: x + y

################################################################################


def calculadora1(operador,x,y):

    if operador == 'sum':
        return x + y
    elif operador == 'res':
        return x - y
    elif operador == 'mul':
        return x * y
    elif operador == 'div':
        return x / y
    else:
        return None

def calculadora2(operator,x,y):

    print("Calculadora")

    # Declaracion de un diccionario

    # dic_Nombre_diccionario = {'clave':dato2,...}  ;   Elementos de un diccionario

    # llamar valores de un diccionario

    # diccionario.keys() : Regresa lista de todas las claves en el diccionario
    # diccionario.items(): Regresa una lista completa de elementos del
    #                      diccionario
    # dic_Services[clave]

    # diccionario.get(clave,por_defecto): Devuelve el valor correspondiente a
    #                                    la clave, en caso de que no exista, no
    #                                    muestra nungun error, sino que retorna
    #                                    el segundo argumento.

    return{
        'sum': lambda: x + y,
        'res': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


num = calculadora2('res', 5, 4)
print(num)

