with open("studenti.txt","r") as file:
    stringhe = file.readlines()
    for stringa in stringhe:
        nuova_str = stringa.strip()
        nuova_str = stringa.split(",")
        nome = nuova_str[0]
        voto = nuova_str[1]
        voto = int(voto)
        if voto >= 8:
            print(nome,"ha preso",voto)

        
