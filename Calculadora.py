# Funciones
def suma(a, b):
    print ("Suma = ", a+b)

def resta(a, b):
    print ("Resta = ", a-b)

def multiplicación(a, b):
    print ("Multiplicación = ", a*b)

def división(a, b):
    print ("División = ", a/b)


# Programa principal

print("Calculadora sencillita, básica y muy elemental.")

num1 = float(input("Escriba el primer número: "))
num2 = float(input("Escriba el segundo número: "))

suma(num1, num2)
resta(num1, num2)
multiplicación(num1, num2)
división(num1, num2)