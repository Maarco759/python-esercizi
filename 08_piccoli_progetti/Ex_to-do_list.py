print("Benvenuto nel menù della tua to-do list")
att = []
while True:
    print("1) Aggiungere un'attività")
    print("2) Visualizzare le attività")
    print("3) Eliminare un'attività")
    print("4) Segnare un'attività come completata")
    print("5) Cercare un'attività")
    print("6) Contare quante attività ci sono")
    print("7) Svuotare tutta la lista")
    print("8) Uscire")
    scelta = int(input("Seleziona una di queste 8 opzioni: "))
    while scelta<1 or scelta>8:
        scelta = int(input("Errore, puoi selezionare solo una di queste 4 opzioni: "))

    if scelta == 1:
        sc = input("Inserisci un attività: ")
        att.append(sc)
    elif scelta == 2:
        if att == []:
            print("Lista delle attività vuota")
        else:
            for azione in att:
                print("-",azione)
    elif scelta == 3:
        if att == []:
            print("Non hai alcuna attività da eliminare")
        else:
            print("Ecco le attività che puoi eliminare")
            for i in range(len(att)):
                print(i+1,"-",att[i])

            scelt = int(input("Quale attività vuoi eliminare? "))
            while scelt < 1 or scelt > len(att):
                print("Scelta non valida")
                scelt = int(input())
                
            azion = att.pop(scelt-1)
            print("Hai eliminato:", azion)
    elif scelta == 4:
        if att == []:
            print("Non hai alcun attivià da segnare come completata")
        else:
            print("Ecco le attività che puoi segnare come completate")
            for i in range(len(att)):
                print(i+1,"-",att[i])
            
            az = int(input("Inserisci quale attività vuoi segnare come completata: "))
            while az<1 or az>len(att):
                print("Scelta non valida")
                az = int(input())
            if att[az-1].startswith("✓"):
                print("L'attività è già segnata come completata")
            else:
                att[az-1] = "✓ " + att[az-1]
                print("Attività segnata come completata")
    elif scelta == 5:
        trovato = False
        q = input("Quale attività vuoi cercare?? ")
        q = q.lower()
        if att == []:
            print("Non è presente alcuna attività da cercare")
        else:
            for attivita in att:
                attivita = attivita.lstrip("✓ ")
                attivita = attivita.lower()
                if attivita == q:
                    trovato = True
            if trovato ==  True:
                print("L'attività è nella to-do list")
            else:
                print("L'attività non è nella to-do list")
    elif scelta == 6:
        lunghezza_lista = len(att)
        print("Nella to-do list ci sono: "+str(lunghezza_lista)+" attività")
    elif scelta == 7:
        if att == []:
            print("La lista è già vuota")
        else:
            att.clear()
            print("Hai rimosso tutte le tue attività")
    elif scelta == 8:
        print("Sei uscito dalla tua to do list")
        break
                
        
