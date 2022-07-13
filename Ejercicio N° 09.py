# Escribe un programa que determine si un año es Bisiesto o Común, de acuerdo a los sigientes parámetros:
# Si es anterior al año 1582, no está dentro del período del calendario Gregoriano.
# Si el número del año no es divisible entre cuatro, es un año común.
# Si el número del año no es divisible entre 100, es un año bisiesto.
# Si el número del año no es divisible entre 400, es un año común.
# De lo contrario, es un año bisiesto.

año = int(input("Introduce un año:"))
if año < 1582:
    print ("No está dentro del período del calendario Gregoriano")
elif año % 4 != 0:
    print ("Año Común")
elif año % 100 != 0:
    print ("Año Bisiesto")
elif año % 400 != 0:
    print ("Año Común")
else:
    print ("Año Bisiesto")
