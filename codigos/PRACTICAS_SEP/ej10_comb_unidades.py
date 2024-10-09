vertidor():
    contador = 0
    print("--- CONVERTIDOR DE UNIDADES ---")
    while contador != 7:
        print ("1. Convertir de metros a Kilometros: ")
        print ("2. Convertir de gramos a kilogramos: ")
        print ("3. Convertir de Celcius a Fahrenheit: ")
        print ("4. Convertir de kilometros a metros: ")
        print ("5. Convertidor de kilogramos a gramos: ")
        print ("6. Convertir de Fahrenheit a Celcius: ")
        elegir = int(input("Elija una opción: "))
        if elegir == 1:
            numero = float(input("Ingrese el valor que quiere convertir: "))
            resultado = FuncionesConvertidor.longitud(numero)
            print ("-----------------------------------------")
            print ("El resultado de la conversión es:" + str(resultado) + " Km")
            print ("-----------------------------------------")
        elif elegir == 2:
            numero = float(input("Ingrese el valor que quiere convertir: "))
            resultado = FuncionesConvertidor.masa(numero)
            print ("-----------------------------------------")
            print ("El resultado de la conversion es: " + str(resultado) + " Kg")
            print ("-----------------------------------------")
        elif elegir == 3:
            numero = float(input("Ingrese el valor que quiere convertir: "))
            resultado = FuncionesConvertidor.temperatura(numero)
            print ("-----------------------------------------")
            print ("El resultado de la conversion es: " + str(resultado) + " ºF")
            print ("-----------------------------------------")
        elif elegir == 4:
            numero = float(input("Ingrese el valor que quiere convertir: "))
            resultado = FuncionesConvertidor.longitud1(numero)
            print ("-----------------------------------------")
            print ("El resultado de la conversion es: " + str(resultado) + " m")
            print ("-----------------------------------------")
        elif elegir == 5:
            numero = float(input("Ingrese el valor que quiere convertir: "))
            resultado = FuncionesConvertidor.masa1(numero)
            print ("-----------------------------------------")
            print ("El resultado de la conversion es: " + str(resultado) + " gr")
            print ("-----------------------------------------")
        elif elegir == 6:
            numero = float(input("Ingrese el valor que quiere convertir: "))
            resultado = FuncionesConvertidor.temperatura1(numero)
            print ("-----------------------------------------")
            print ("El resultado de la conversion es: " + str(resultado)+ " ºC")
            print ("-----------------------------------------")
        else:
            print ("Eso es todo, gracias :)")
            break
convertidor()