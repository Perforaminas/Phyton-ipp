def juego():
    try:
        num = int(input("Ingrese un número entero del 1 al 9: "))
        if num < 1 or num > 9:
            raise ValueError
        i = 1
        while i <= 100:
            if i % num!= 0:
                print(i)
            i += 1
    except ValueError:
        print("Error: Ingrese un número entero del 1 al 9.")

juego()