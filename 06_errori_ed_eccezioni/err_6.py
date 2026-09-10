def aggiungi_studente():
    with open("studenti_nuovo.txt", "a") as file:
        while True:
            try:
                nuovo_stud = input("Inserisci il nome dello studente:")
                nuovo_stud = nuovo_stud.strip()
                while nuovo_stud == "":
                    print("Nome non valido")
                    nuovo_stud = input("Reinserisci il nome dello studente:")
                nuovo_voto = float(input("Inserisci il voto: "))
                while nuovo_voto<0 or nuovo_voto>10:
                    nuovo_voto = float(input("Reinserisci il voto: "))
                file.write(nuovo_stud+","+str(nuovo_voto)+"\n")
                break
            except ValueError:
                print("Input non valido")

def calcola_media():
    with open("studenti_nuovo.txt", "r") as file:
        contS = 0.0
        numV = 0
        for riga in file:
            dati = riga.split(",")
            voto = dati[1]
            voto = float(voto)
            contS += voto
            numV += 1
        try:
            media = contS / numV
            print("La media complessiva di tutti i voti è di: ",media)
        except ZeroDivisionError:
            print("Non ci sono studenti nel file, impossibile calcolare la media.")

def voto_massimo():
    with open("studenti_nuovo.txt", "r") as file:
        primo = True
        mass = 0.0
        for riga in file:
            dati = riga.split(",")
            voto = dati[1]
            voto = float(voto)
            if primo:
                mass = voto
                primo = False
            if voto > mass:
                mass = voto
        if primo:
            print("Nessuno studente nel file")
        else:
            print("La media complessiva degli studenti è: ",mass)
    

def voto_minimo():
    with open("studenti_nuovo.txt", "r") as file:
        minim = 0.0
        primo = True 
        for riga in file:
            dati = riga.split(",")
            voto = dati[1]
            voto = float(voto)
            if primo:
                minim = voto
                primo = False
            if voto < minim:
                minim = voto
        if primo:
            print("Nessuno studente nel file")
        else:
            print("Il voto più basso è: ",minim)

def studenti_promossi():
    with open("studenti_nuovo.txt", "r") as file:
        contP = 0
        for riga in file:
            dati = riga.split(",")
            try:
                voto = dati[1]
                voto = float(voto)
                if voto >= 6:
                    contP += 1
            except ValueError:
                print("Riga non valida")
        print("Gli studenti promossi sono: ",contP)

def modifica_voto():
    with open("studenti_nuovo.txt", "r") as file:
        cerca_nome = input("Inserisci il nome dello studente di cui vuoi modificare il voto: ")
        while cerca_nome == "":
            print("Nome non valido")
            cerca_nome = input("Reinserisci il nome dello studente:")
        cerca_nome = cerca_nome.lower()
        nome_trovato = False
        righe = file.readlines()
        for indice,riga in enumerate(righe):
            dati = riga.split(",")
            nome_originale = dati[0]
            nome = nome_originale.lower()
            if cerca_nome == nome:
                nome_trovato = True
                while True:
                    try:
                        nuovo_voto = float(input("Inserisci il un voto da 0 a 10: "))
                        while nuovo_voto<0 or nuovo_voto>10:
                            nuovo_voto = float(input("Devi inserire un voto compreso tra 0 e 10: "))
                        nuova_riga = nome_originale+","+str(nuovo_voto)+"\n"
                        righe[indice] = nuova_riga
                        break
                    except ValueError:
                        print("Errore devi inserire un numero compreso tra 0 e 10")
                        continue
        if nome_trovato:
            with open("studenti_nuovo.txt", "w") as file:
                for riga in righe:
                    file.write(riga)
        else:
            print("Studente non trovato")

def elimina_studente():
    with open("studenti_nuovo.txt", "r") as file:
        cerca_nome = input("Inserisci il nome dello studente che vuoi eliminare: ")
        while cerca_nome == "":
            print("Nome non valido")
            cerca_nome = input("Reinserisci il nome dello studente:")
        cerca_nome = cerca_nome.lower()
        nome_trovato = False
        righe = file.readlines()
        for indice,riga in enumerate(righe):
            if riga.strip()== "":
                continue
            else:
                dati = riga.split(",")
                nome = dati[0].lower()  
            if cerca_nome == nome:
                if len(dati) == 2:
                    nome_trovato = True
                    nome_originale = dati[0]
                    voto_originale = dati[1]
                else:
                    continue
                print("Hai eliminato:", nome_originale,voto_originale)
                righe.pop(indice)
                break
        if nome_trovato:
            with open("studenti_nuovo.txt", "w") as file:
                for riga in righe:
                    file.write(riga)
        else:
            print("Studente non trovato")
     
def cerca_studente():
    with open("studenti_nuovo.txt", "r") as file:
        voto_trovato = False
        cerca_nome = input("Inserisci lo studente che stai cercando: ")
        cerca_nome = cerca_nome.lower().strip()
        for studente in file:
            if studente.strip() == "":
                continue
            studente = studente.lower()
            studente = studente.split(",")
            if len(studente) == 2:
                if studente[0] == cerca_nome:
                    voto_trovato = True
                    voto = studente[1]
                    break
        if voto_trovato == True:
            print("Il voto di questo studente è: ",voto)
        else:
            print("Studente non trovato")
            
def mostra_studenti():
    with open("studenti_nuovo.txt", "r") as file:
        for riga in file:
            print(riga.strip())

def esci():
    print("Sei uscito dal gestionale studenti")

while True:
    print("Benvenuto nel gestionale studenti: ")
    print("1)Aggiungi studente")
    print("2)Mostra studenti")
    print("3)Cerca studente")
    print("4)Calcola la media")
    print("5)Trova il voto massimo")
    print("6)Trova il voto minimo")
    print("7)Conta studenti promossi")
    print("8)Modifica voto")
    print("9)Elimina studente")
    print("10)Esci")
    while True:
        try:
            scelta = int(input("Scegli una delle opzioni 1-10: "))
            if scelta >= 1 and scelta <= 10 :
                break
            else:
                print("Scelta non valida")
        except ValueError:
            print("Scelta non valida")
    if scelta == 1:
        aggiungi_studente()
    elif scelta == 2:
        mostra_studenti()
    elif scelta == 3:
        cerca_studente()
    elif scelta == 4:
        calcola_media()
    elif scelta == 5:
        voto_massimo()
    elif scelta == 6:
        voto_minimo()
    elif scelta == 7:
        studenti_promossi()
    elif scelta == 8:
        modifica_voto()
    elif scelta == 9:
        elimina_studente()
    elif scelta == 10:
        esci()
        break
        
        

