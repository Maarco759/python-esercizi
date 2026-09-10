with open("studenti_nuovo.txt","a") as file:
    nome = input("Inserisci il nome: ")
    voto = input("Inserisci il voto: ")
    file.write(nome+","+voto+"\n")
with open("studenti_nuovo.txt", "r") as file:
    for riga in file:
        print(riga.strip())
        
