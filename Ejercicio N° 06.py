# Escribe un programa que pida ingresar el nombre del estudiante,
# que tome las tres notas y promedie la nota final del curso, con dos decimales.
# Si la nota es igual o superior a 7, informar el nombre del estudiante junto a la leyenda "Estás aprobado".
# Si la nota es inferior a 7, informar "Lo siento, (estudiante). Debes continuar estudiando para poder aprobar".

def promedio(n1, n2, n3):
    return(n1 + n2 + n3)/3

nombre = input("Ingresa tu nombre: ")
   
n1 = float(input("Primera Nota: "))
n2 = float(input("Segunda Nota: "))
n3 = float(input("Tercera Nota: "))
     
final = promedio(n1, n2, n3)
print("El promedio es:", round (final,2))

if final >= 7:
    print(nombre,"estás APROBADO.")
else:
    print("Lo siento,", nombre + ". Debes continuar estudiando para poder aprobar.")