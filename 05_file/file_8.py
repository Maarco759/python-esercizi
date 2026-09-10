with open("studenti_nuovo.txt","r") as file:
    contS = 0
    for riga in file:
        nuova_riga = riga.strip()
        nuova_riga = nuova_riga.split(",")
        nome = nuova_riga[0]
        voto = nuova_riga[1]
        voto = int(voto)
        if voto >= 8:
            contS += 1
    print("Gli studenti con almeno 8 sono: ",contS)
    
