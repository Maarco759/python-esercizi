while True:
    try:
        numero = int(input("Inserisci un numero: "))
        print(100/numero)
        break
    except ValueError:
        print("Input non valido")
    except ZeroDivisionError:
        print("Non puoi usare zero")
    

