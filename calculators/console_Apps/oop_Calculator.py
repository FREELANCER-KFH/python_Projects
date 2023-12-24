#class comandos_Sistema:
class opp_Calculator:
    def __init__(self):
        pass

    def limpiar_Pantalla(self):
        import os
        return os.system("cls")
    
    def finalizar_Proceso(self, condicion):
        self.opcion_Incorrecta = 'Opcion incorrecta, favor digitar una opcion valida.'
        self.salida_Proceso = 'Precione cualquier tecla para salir del proceso...'
        self.salida_Programa = 'Gracias por usar la calculadora KFH'
        self.tecla_Volver = 'Presione cualquier tecla para volver al menu anterior...'
        self.tecla_Salir = 'Presione cualquier tecla para salid del programa...'
        if(condicion == 0):
            print(self.opcion_Incorrecta)
        elif(condicion == 1):
            print(self.opcion_Incorrecta)
            input(self.tecla_Volver)
            self.menu_Principal()
        elif(condicion == 2):
            input(self.salida_Proceso)
        elif(condicion == 3):
            print(self.salida_Programa)
            input(self.tecla_Salir)
            self.limpiar_Pantalla()
            exit()

    def desea_Continuar(self):
        while True:
            continuar = input('Desea continuar con la operacion? (S/N): ')
            if(continuar == 'S' or continuar == 's'):
                break
            elif(continuar == 'N' or continuar == 'n'):
                self.finalizar_Proceso(2)
                self.menu_Principal()
            else:
                self.finalizar_Proceso(0)
                continue

    def calculadora(self, valor_Actual, valor_Nuevo, op):
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
        return resultado_Final
    
    def operacion(self, operador):
        resultado = 0
        while True:
            if(resultado == 0):
                resultado += self.calculadora(self.validacion_Digito(input('Digite el primer numero: ')), self.validacion_Digito(input('Digite el segundo numero: ')), operador)
            else:
                resultado = self.calculadora(resultado, self.validacion_Digito(input('Digite otro numero: ')), operador)
            print('El resultado de la operacion es: ', int(resultado))
            self.desea_Continuar()

    def iniciar_Proceso(self, codigo):
        if(codigo <= 0 or codigo >= 8):
            self.finalizar_Proceso(1)
        else:
            match codigo:
                case 7:
                    self.finalizar_Proceso(3)
                case 1:
                    operador = '+'
                    self.operacion(operador)
                case 2:
                    operador = '-'
                    self.operacion(operador)
                case 3:
                    operador = '*'
                    self.operacion(operador)
                case 4:
                    operador = '/'
                    self.operacion(operador)
                case 5:
                    operador = '%'
                    self.operacion(operador)
                case 6:
                    operador = '^'
                    self.operacion(operador)

    def validacion_Digito(self, digito):
        if(digito.isdigit()):
           return float(digito)
        else:
           return 0
        
    def menu_Principal(self):
        while True:
            self.limpiar_Pantalla()
            print('Bienvenido a la calculadora KFH')
            print("")
            print('Menu de operaciones:')
            print('digite 1 para la suma: ')
            print('digite 2 para la resta: ')
            print('digite 3 para la multiplicacion: ')
            print('digite 4 para el cociente de la division: ')
            print('digite 5 para el reciduo de la division: ')
            print('digite 6 para la potencia: ')
            print('digite 7 para salir del programa: ')
            codigo_Menu = self.validacion_Digito(input())
            return self.iniciar_Proceso(codigo_Menu)
        
    def programa_Principal(self):
        self.menu_Principal()


#Instancia de la clase
calculadora = opp_Calculator()

#Inicio del programa
calculadora.menu_Principal()