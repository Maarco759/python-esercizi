num_giusto = 67
tentativi = 0
while tentativi<5:
    num_utente = float(input("Inserisci un numero: "))
    if num_utente == num_giusto:
        print("Numero corretto!")
        break
    else:
        print("Numero errato, riprova")
        tentativi += 1
        print("Ti rimangono "+str(5-tentativi)+" tentativi")
        if tentativi ==  5:
            print("Troppi tentativi, gioco finito")

    
