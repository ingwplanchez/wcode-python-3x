
# Funciones con parametros

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

##
## Pseudocodigo:

##  FUNCION:
##        Instruciones
##  Fin de FUNCION

## Instrucciones
## Hacer FUNCION
## Instrucciones

################################################################################

# Declaracion de variables: Globales

##  str_Continuar : Variable para saber si se continua con el programa
##  str_Opcion    : Almacena la operacion a ejecutar
##  int_Numero1   : Primer valor solicitado por al usuario
##  int_Numero2   : Segundo Valor solicitado al usuario

# Variables Globales

str_Continuar = "S"
str_Opcion = ''

int_Numero1 = 0
int_Numero2 = 0

# Declaracion de Funciones:

################################################################################
################################################################################

def str_main():

    """
    Descripcion : Funcion principal
    Parametros  : Sin parametros
    Retorna     : Un caracter para continuar o no con el programa
    """

    print(str_main.__name__)
    print(str_main.__doc__)

    print("\nPROGRAMA PRINCIPAL\n")

    # Solicitud de Datos al Usuario
    int_Numero1 = int(input('Introduce El primer numero: '))
    int_Numero2 = int(input('Introduce El Segundo numero: '))

    # Almacena la Opcion a Ejecutar
    str_Opcion = str_menu()

    #Ejecuta la operacion Seleccionada
    operaciones(str_Opcion,int_Numero1,int_Numero2)

    # Se pregunta al usuario si desea Continuar
    # Variable local
    str_Continuar = input(('Desea Continuar: S/N:'))
    return str_Continuar

################################################################################
################################################################################

def str_menu():

    """
    Descripcion : Imprime un menu de opciones
    Parametros  : Sin parametros
    Retorna     : Devuelve la operacion a ejecutar
    """

##    print(str_menu.__name__)
##    print(str_menu.__doc__)

    print("\nMENU DE OPCIONES\n")

    print ("1) SUMA.")
    print ("2) RESTA.")
    print ("3) MULTIPLICACION.")
    print ("4) DIVISION.\n")
    
    # Variable Local
    str_Operacion = input('Teclea la opcion y pulsa Enter: ')
    return str_Operacion

################################################################################
################################################################################

def operaciones(str_operacion,int_valor1, int_valor2):

    """
    Descripcion : Ejecuta la operacion e imprime el resultado
    Parametros  : str_operacion,int_valor1, int_valor2

      str_operacion   : Caracter que guarda la operacion
      int_valor1      : Primer dato introducido por el usuario
      int_valor2      : Segundo dato introducido por el usuario

    Retorna     : No devuelve parametros
    """
##    print(operaciones.__name__)
##    print(operaciones.__doc__)

    if str_operacion == '1':
        print("\nEl resultado es: %1.2f\n"%(int_valor1 + int_valor2))
        return

    elif str_operacion == '2':
        print("\nEl resultado es: %1.2f\n"%(int_valor1 - int_valor2))
        return

    elif str_operacion == '3':
        print("\nEl resultado es: %1.2f\n"%(int_valor1 * int_valor2))
        return

    elif str_operacion == '4':
        print("\nEl resultado es: %1.2f\n"%(int_valor1 / int_valor2))
        return

    else:
        print("No es una opcion valida.\n")
        return

################################################################################
################################################################################

### Inicio del programa:

while str_Continuar == 's' or  str_Continuar =='S':

    str_Continuar = str_main()

print("\nFIN DEL PROGRAMA\n")

