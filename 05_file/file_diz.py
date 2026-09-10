studenti = {}
with open("studenti_nuovo.txt", "r") as file:
    for riga in file:
        nuova_str = riga.strip()
        nuova_str = nuova_str.split(",")
        nome = nuova_str[0]
        voto = nuova_str[1]
        voto = float(voto)
        studenti[nome] = voto
    print(studenti)
