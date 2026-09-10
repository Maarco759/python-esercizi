with open("studenti_nuovo.txt","r") as file:
    with open("promossi.txt","w") as nuovo_file:
        for riga in file:
            nuova_str = riga.strip()
            nuova_str = nuova_str.split(",")
            nome = nuova_str[0]
            voto = nuova_str[1]
            voto = int(voto)
            if voto >= 6:
                nuovo_file.write(nome+","+str(voto)+"\n")
