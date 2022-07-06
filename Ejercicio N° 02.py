# Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable.
# Luego, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable.
# En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario.
# Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]".
 
# Ejemplo de ejecución:

# Primer número (con decimales): 25.3
# Segundo número (entero): 4
# El resultado de la suma es 29.3

var_1 = float(input("Ingresá un numero con decimales: "))
var_2 = int(input("Ingresá un numero entero: "))
suma = (var_1 + var_2)
print("El resultado de la suma es ", suma)