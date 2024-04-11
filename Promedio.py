"""
Realiza un programa que reciba tres numeros por teclado y calcule su promedio, se debe mostrar el resultado en pantalla.

- reciba tres numeros por teclado
- calcule su promedio
- se debe mostrar el resultado en pantalla

"""

# Inicializar variables para almacenar los numeros ingresados por el usuario 

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

# Calcular el promedio de los numeros ingresados

promedio = (numero1 + numero2 + numero3) / 3

# Mostrar el resultado en pantalla

print(f"El promedio de la suma de las notas es: ", promedio)
