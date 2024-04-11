try:    
    rutSindigito = input("Ingresa tu rut: ")
    if not rutSindigito.isdigit or len(rutSindigito) != 8:
        raise  ValueError("El rut debe ser un número de 8 dígitos")
    #multiplicación por la secuencia de 2 a 7
    suma = (int(rutSindigito[7]) * 2 +
            int(rutSindigito[6]) * 3 +
            int(rutSindigito[5]) * 4 +
            int(rutSindigito[4]) * 5 +
            int(rutSindigito[3]) * 6 +
            int(rutSindigito[2]) * 7 +
            int(rutSindigito[1]) * 2 +
            int(rutSindigito[0]) * 3)    
    #Calcular el resto de la división de la suma por 11
    resto = suma % 11
    #Calcular el digito verificador
    digitoVerificador = 11 - resto
    #convertimos el digito verificador a string
    if digitoVerificador == 10:
        digitoVerificador = "k"
    elif digitoVerificador == 11:
        digitoVerificador = 0
    print ("El digito verificador es: ", digitoVerificador)
except ValueError as e:
    #manejar la excepción y mostrar un mensaje de error 
    print("Error: ", e)






