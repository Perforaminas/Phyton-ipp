
try:

    rutSindigito = input("Ingrese su Rut: ")

    #verificamos que el rut tenga una longitud de 8

    if not rutSindigito.isdigit or len(rutSindigito) != 8:
        raise ValueError("El rut debe ser de 8 digitos")
    
    #inicializamos la suma 

    suma = 0 
    multiplicador = 2

    # recorrer cada digito del rut de derecha a izquierda 

    for digito in reversed(rutSindigito):
        # sumas al total la multiplicación del digito por su multiplicación correspondiente (2 a 7)
        suma += int(digito) * multiplicador 

        # si el multiplicador es 7, se reinicia a 2

        multiplicador += 1
        if multiplicador >7:
            multiplicador = 2

    # calculamos el resto 

    resto = suma % 11

    #calculamos el digito verificador 

    digitoVerificador = 11 - resto

    #convertir el digito de 10 = k y 11 = 0

    if digitoVerificador == 10:
        digitoVerificador = "K"
    elif digitoVerificador == 11:
        digitoVerificador = "0"

    print("El digito verificador es: ",digitoVerificador)


except ValueError as e:
    #manejar la excepción y mostrar un mensaje de error 
    print("Error: ",e)




