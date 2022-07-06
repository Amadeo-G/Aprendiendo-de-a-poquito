# Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por un auto y la cantidad de litros de combustible que consumió durante ese recorrido.
# Mostrar el consumo de combustible por kilómetro.
 
# Ejemplo de ejecución:

# Kilómetros recorridos: 120
# Litros de combustible gastados: 9.6
# El consumo por kilómetro es de 0.08 litros.

k = float(input("Kilometros recorridos: "))
g = float(input("Litros de combustible gastados: "))
c = g/k
print("El consumo por kilómetro es de", c, "litros.")