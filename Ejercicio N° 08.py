# Escribe una calculadora de impuesto de acuerdo a los siguientes parámetros:
# Si el ingreso del ciudadano no es superior a 90.000 pesos, el impuesto es igual al 18% del ingreso menos 520 pesos.
# Si el ingreso es superior a esta cantidad, el impuesto es igual a 14.500 pesos, más el 32% del excedente sobre 90.000 pesos.
# Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero).

ingresos = float(input("Introduce el ingreso anual:"))
if ingresos <= 90000:
    impuestos = ingresos * (18/100) - 520
else:
    ingresos > 90000:
    impuestos = 14500 + ((ingresos - 90000)*32/100)
if impuestos < 0:
    impuestos = 0.0

impuestos = round(impuestos, 0)
print("El impuesto es equivalente a:", impuestos, "pesos")
