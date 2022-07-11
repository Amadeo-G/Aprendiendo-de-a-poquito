# Partiendo del valor de una compra sin IVA (del 21%), calcular el valor total de la compra, y el valor del IVA.
# Redondear los valores de salida, a dos decimales.

def IVA (n1, n2):
    return (n1 * n2)

n1 = float(input("Valor de la compra sin IVA: "))
n2 = 1.21

cálculo = IVA (n1, n2)
print("El valor total de la compra con IVA incluido es", round(cálculo,2))
print("El valor del IVA es", round(cálculo - n1, 2))
