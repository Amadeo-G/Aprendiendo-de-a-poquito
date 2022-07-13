# Escribe un programa en el que el usuario debe adivinar un número entre el 1 y el 15, elegido por tí
# y almacenado en la variable num_elegido.
# Solicitale que ingrese un número
# Utilliza el bucle While. Pide un nuevo intento ante cada fallo.
# Si el usuario acierta, muestra en pantalla: "¡Bien hecho! ¡Lo has logrado!"

num_elegido = 7
print("Adivina el número que elegí entre 1 y 10")
n1=int(input("Ingresa el número: "))
if n1 > 10 or n1 <1:
    print("Número no válido. Debe estar entre 1 y 10")
while n1 != num_elegido:
    print("Sigue intentando")
    n1=int(input("Ingresa otro número: "))
    if n1 == num_elegido:
        print("¡Bien hecho! ¡Lo has logrado!")