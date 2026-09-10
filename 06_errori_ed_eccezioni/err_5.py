with open("studenti_nuovo.txt", "r") as file:
    voto_trovato = False
    cerca_nome = input("Inserisci lo studente che stai cercando: ")
    cerca_nome = cerca_nome.lower().strip()
    for studente in file:
        studente = studente.lower()
        studente = studente.split(",")
        if studente[0].lower() == cerca_nome:
            voto_trovato = True
            voto = studente[1]
            break
    if voto_trovato == True:
        print("Il voto di questo studente è: ",voto)
    else:
        print("Studente non trovato")
