"""
Supón que un ramo tiene las siguientes evaluaciones:
- 3 tareas en laboratorio, estas valen un 15% del curso.
- 3 tareas en clase, que valen un 15% del curso.
- 2 notas solemnes cada una un 35%.
- Elabora un programa que, ingresando todas las notas, entregue el promedio del ramo.

"""
# Definir las variables y tipos de datos 

lab1 = float(input("Ingresa la nota del laboratorio 1: "))
lab2 = float(input("Ingresa la nota del laboratorio 2: "))
lab3 = float(input("Ingresa la nota del laboratorio 3: "))

# Definir las 3 notas de las tareas 

tarea1 =float(input("\nIngrese la nota de la tarea 1: "))
tarea2 =float(input("Ingrese la nota de la tarea 2: "))
tarea3 =float(input("Ingrese la nota de la tarea 3: "))

# Definir las 2 notas de las solemnes 

solemne1 =float(input("\nIngrese la nota de solemne 1: "))
solemne2 =float(input("Ingrese la nota de solemne 2: "))

# Calcular el promedio del ramo 

promedioLaboratorio = (lab1 + lab2 + lab3) / 3 
promedioTareas = (tarea1 + tarea2 + tarea3) / 3

# Calcular el promedio del ramo

nota_presentacion = (promedioLaboratorio * 0.15) + (promedioTareas * 0.15) + (solemne1 * 0.35) + (solemne2 * 0.35)

# Mostrar los resultados
 
print(f"El promedio de Laboratorio = {promedioLaboratorio}")
print(f"El promedio de Tareas = {promedioTareas}\n")
print(f"El promedio de la nota de presentacion = {nota_presentacion}")

