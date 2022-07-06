# Escribí un programa que solicite el ingreso de dos números enteros diferentes y muestre en pantalla al mayor de los dos.

# Ejemplo de ejecución:

# Primer número: 100
# Segundo número: 140
# 140 es mayor

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))
if n1>n2:
    print(n1,"es mayor.")
else:
    print(n2,"es mayor.")