#Funcion limpiar_Pantalla
def limpiar_Pantalla():
    import os
    return os.system("cls")

#Funcion calculadora
def calculadora(valor_Actual, valor_Nuevo, op):
    match op:
        case "+":
            resultado_Final = valor_Actual + valor_Nuevo
        case "-":
            resultado_Final = valor_Actual - valor_Nuevo
        case "*":
            resultado_Final = valor_Actual * valor_Nuevo
        case "/":
            if(valor_Nuevo == 0):
                print('No se puede dividir por cero')
                resultado_Final = valor_Actual
            else:
                resultado_Final = valor_Actual / valor_Nuevo
        case "%":
            if(valor_Nuevo == 0):
                print('No se puede dividir por cero')
                resultado_Final = valor_Actual
            else:
                resultado_Final = valor_Actual % valor_Nuevo
        case "^":
            resultado_Final = valor_Actual ** valor_Nuevo
        case '√':
            if(valor_Nuevo == 0):
                print('No se puede dividir por cero')
                resultado_Final = valor_Actual
            else:
                resultado_Final = valor_Actual ** (1 / valor_Nuevo)
    return resultado_Final

#Funcion desea_Continuar
def desea_Continuar():
    while True:
        continuar = input('Desea continuar con la operacion? (S/N): ')
        if(continuar == 'S' or continuar == 's'):
            break
        elif(continuar == 'N' or continuar == 'n'):
            finalizar_Proceso(2)
            menu_Principal()
        else:
            finalizar_Proceso(0)
            continue

#Funcion operacion
def operacion(operador):
    resultado = 0
    while True:
        if(resultado == 0):
            resultado += calculadora(validacion_Digito(input('Digite el primer numero: ')), validacion_Digito(input('Digite el segundo numero: ')), operador)
        else:
            resultado = calculadora(resultado, validacion_Digito(input('Digite otro numero: ')), operador)
        print('El resultado de la operacion es: ', int(resultado))
        desea_Continuar()

#Funcion finalizar_Proceso
def finalizar_Proceso(condicion):
    opcion_Incorrecta = 'Opcion incorrecta, favor digitar una opcion valida.'
    salida_Proceso = 'Precione cualquier tecla para salir del proceso...'
    salida_Programa = 'Gracias por usar la calculadora KFH'
    tecla_Volver = 'Presione cualquier tecla para volver al menu anterior...'
    tecla_Salir = 'Presione cualquier tecla para salid del programa...'
    if(condicion == 0):
        print(opcion_Incorrecta)
    elif(condicion == 1):
        print(opcion_Incorrecta)
        input(tecla_Volver)
        menu_Principal()
    elif(condicion == 2):
        input(salida_Proceso)
    elif(condicion == 3):
        print(salida_Programa)
        input(tecla_Salir)
        limpiar_Pantalla()
        exit()

#Funcion iniciar_Proceso
def iniciar_Proceso(codigo):
    if(codigo < 1 or codigo > 8):
        finalizar_Proceso(1)
    else:
        match codigo:
            case 8:
                finalizar_Proceso(3)
            case 1:
                operador = '+'
                operacion(operador)
            case 2:
                operador = '-'
                operacion(operador)
            case 3:
                operador = '*'
                operacion(operador)
            case 4:
                operador = '/'
                operacion(operador)
            case 5:
                operador = '%'
                operacion(operador)
            case 6:
                operador = '^'
                operacion(operador)
            case 7:
                operador = '√'
                operacion(operador)

#Funcion validacion_Digito
def validacion_Digito(digito):
        if(digito.isdigit()):
           return float(digito)
        else:
           return 0
        
#Funcion menu_Principal
def menu_Principal():
    while True:
        limpiar_Pantalla()
        print('Bienvenido a la calculadora KFH')
        print("")
        print('Menu de operaciones:')
        print('digite 1 para la suma: ')
        print('digite 2 para la resta: ')
        print('digite 3 para la multiplicacion: ')
        print('digite 4 para el cociente de la division: ')
        print('digite 5 para el reciduo de la division: ')
        print('digite 6 para la potencia: ')
        print("digite 7 para la raiz:")
        print('digite 8 para salir del programa: ')
        codigo_Menu = validacion_Digito(input())
        return iniciar_Proceso(codigo_Menu)

#Funcion programa_Principal
def programa_Principal():
    menu_Principal()

#Inicio del programa
programa_Principal()