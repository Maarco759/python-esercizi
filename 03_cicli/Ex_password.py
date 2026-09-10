password_corretta = "67"
tentativi = 0
while tentativi<3:
    password_utente = input("Inserisci la password: ")
    if password_utente == password_corretta:
        print("Password indovinata, accesso eseguito")
        break
    else:
        print("Password errata, riprova")
        tentativi += 1
        print("Ti rimangono "+str(3-tentativi)+" tentativi")
        if tentativi == 3:
            print("Troppi tentativi, accesso fallito")
        
    
