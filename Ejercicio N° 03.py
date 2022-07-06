# Escribí un programa que le solicite dos números al usuario, almacenados en dos variables distintas.
# Sumá esos números y, en otra variable, almacená el resultado.
# Mostrá ese resultado en pantalla.
# Luege, pedile al usuario que ingrese un tercer número y almacenalo en una nueva variable.
# Finalmente, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
 
# Ejemplo de ejecución:

# Ingresá un número: 2
# Ingresá otro número: 5
# Suman: 7
# Ingresá un nuevo número: 4
# Multiplicación de la suma por el último número: 28

n1 = int(input("Ingresá un número: "))
n2 = int(input("Ingresá otro número: "))
suma = n1 + n2
print("Suman: ", suma)
n3 = int(input("Ingresá un nuevo número: "))
print("Multiplicación de la suma por el último número: ", suma * n3)



