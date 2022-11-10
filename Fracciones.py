#Objeto
class Fraction:

    #Atributos
    numerator=0
    denominator=1

    #Metodos

    def __init__(self, numerator, denominator):   #Inciar variables que se utilizaran
        self.num = numerador                       #Numerador
        self.den = denominador                      #Denominador

    def __add__(self, second):                               #Funcion de suma de fracciones
        num = self.num * second.den + self.den * second.num  #Calculo para conseguir en resultado el numerador
        den = self.den * second.den                         #Calculo para conseguir en resultado el denominador
        return Fraction(num, den)                          #Devolver el resultado que de la ecuacion anterior para mostrarla en pantalla
    
    def __sub__(self, second):                              #Funcion de resta de fracciones
        num = (self.num * second.den) - (self.den * second.num)   #Calculos linea 22 y 23 para conseguir la nueva fraccion
        den = self.num * second.den
        return Fraction(num, den)

    def __mul__(self, second):                           #Funcion de multiplicacion de fracciones
        num = self.num * second.num
        den = self.den * second.den
        return Fraction(num, den)
     
    def __truediv__(self, second):                  #Funcion de division de fracciones
        num = self.num * second.den
        den = self.den * second.num
        return Fraction(num, den)

    def __str__(self):                              #Funcion para devolver la ecuacion en forma de String
        return str(self.num)+"/"+str(self.den)

print("Fraccion 1")                                           #Pedir los valores para la primera fraccion 

num1 = int(input("Ingrese valor del numerador 1\n"))
den1 = int(input("Ingrese valor del denominador 1\n"))
if den1 == 0:
    raise Exception("**Ingrese en el denominador un valor distinto a 0**")      #En caso del usuario ingresar un valor 0 en el denominador devolver un error orientando al usuario

print("Fraccion 2")                                              #Pedir los valores para la segunda fraccion 

num2 = int(input("Ingrese valor del numerador 2\n"))
den2 = int(input("Ingrese valor del denominador 2\n"))
if den2 ==0 :
    raise Exception("**Ingrese en el denominador un valor distinto a 0**")     #En caso del usuario ingresar un valor 0 en el denominador devolver un error orientando al usuario


a = Fraction(num1, den1)    #Se agrupa los valores dado por el usuario en una variable con la clase "Fraction"
b = Fraction(num2, den2)

print("\n")
print("¿Que operacion desea realizar?")      #Preguntar al usuario que operacion desea que se realice

print("Suma, ingresar `+` ")
print("Resta, ingresar `-`")
print("Multiplicacion, ingresar `*`")
print("Division, ingresar `/`\n")

choice = input("Ingresar: ")   #Signo que ingresara el usuario para proceder con el calculo de fracciones
print("\n")
print("Resultado:")

match choice:           #Dependiendo de la eleccion del usuario se realizara alguna operacion con los valores dados por el usuario
    case "+":   #Suma
        print(a + b)
    case "-":   #Resta
        print(a - b)
    case "*":   #Multiplicacion
        print(a * b)
    case "/":   #Division
        print(a / b)
