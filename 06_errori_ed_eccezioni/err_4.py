with open("studenti_nuovo.txt", "a") as file:
    while True:
        try:
            nuovo_stud = input("Inserisci il nome dello studente: ")
            nuovo_voto = float(input("Inserisci il voto: "))
            file.write(nuovo_stud+","+str(nuovo_voto)+"\n")
            break
        except ValueError:
            print("Input non valido")

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



