"""
Debes crear un programa que dibuje una matriz, según las siguientes consideraciones:

1. Solicitar la cantidad de filas.
2. Solicitar la cantidad de columnas.
3. Dibujar las filas y columnas solicitadas.

"""

#Solicitar las cantidad de filas.
#Crear variables, con la cantidad de filas y columnas.

filas = int(input("Ingresa la cantidad de filas:"))

#Solicitar las cantidad de columnas.

columnas = int(input("Ingresa la cantidad de columnas:"))

#Iterar sobre las filas mas uno para incluir las lineas horizontales.
#Crear un ciclo for para las filas y columnas.
#Entregamos el codigo para que se imprima la matriz.


for i in range(filas * 2 + 1):
    for j in range(columnas * 2 + 1):
        #Determina si se encuentra en una esquina.
        if i % 2 == 0 and j % 2 == 0:
            #Imprime el caracter de esquina.
            print("+", end="")
        #Determina si se encuentra en una linea horizontal.
        elif i % 2 == 0:
            #Imprime el caracter de linea horizontal.
            print("---", end="")
        #Determina si se encuentra en un borde vertical.
        elif j % 2 == 0:
            #Imprime el caracter de borde vertical.
            print("|  ", end="")
        #Determinar en el caso que no se encuentre en una esquina, ni en una linea horizontal, ni en un borde vertical.
        #Imprime el caracter de espacio.
        else:
            print(" ", end="")
    print()




