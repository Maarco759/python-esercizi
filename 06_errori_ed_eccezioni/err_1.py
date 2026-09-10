try:
    numero = int(input("Inserisci un numero: "))
    print("Hai inserito:", numero)
except ValueError:
    print("Hai inserito qualcosa che non è un numero")
