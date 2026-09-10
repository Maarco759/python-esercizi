voti = {}


def aggiungi_studente(voti):
    nome = input("Inserisci il nome dello studente:  ")
    voto = float(input("Inserisci un voto (1-10) allo studente: "))
    voti[nome] = voto


def visualizza_voti(voti):
    for nome, voto in voti.items():
        print(nome,"-",voto)


def modifica_voto(voti):
    if voti == {}:
        print("Gestione voti vuota")
    else:
        print("Ecco gli studenti: ")
        studenti = list(voti.keys())
        for i in range(len(studenti)):
            print(i+1,"-",studenti[i])
        stud = int(input("A quale studente vuoi modificare il voto? "))
        while stud < 1 or stud > len(voti):
            stud = int(input("Scelta non valida, reinserisci: "))
        mod_voto = studenti[stud-1]
        voti[mod_voto] = float(input("Inserisci il nuovo voto: "))


def elimina_studente(voti):
    if voti == {}:
        print("Gestione voti vuota")
    else:
        print("Ecco gli studenti: ")
        studenti = list(voti.keys())
        for i in range(len(studenti)):
            print(i+1,"-",studenti[i])
        scelt = int(input("Quale studente vuoi eliminare?? "))
        while scelt < 1 or scelt > len(voti):
            scelt = int(input("Scelta non valida, reinserisci: "))
        nome_studente = studenti[scelt-1]
        voto_studente = voti.pop(nome_studente)
        print("Hai rimosso: ",nome_studente,"-",voto_studente)

    
def calcola_media(voti):
    somma = 0.0
    contS = 0
    media = 0.0
    for voto in voti.values():
        somma += voto
        contS += 1
    media = somma / contS
    print("La media totale generale è di: ",media)

            
def trova_massimo(voti):
    lista_voti = list(voti.values())
    massimo = lista_voti[0]
    for voto in voti.values():
        if voto > massimo:
            massimo = voto
    print("Il voto massimo è: ",massimo)

            
def trova_minimo(voti):
    lista_voti = list(voti.values())
    minimo = lista_voti[0]
    for voto in voti.values():
        if voto < minimo:
            minimo = voto
    print("Il voto minimo è: ",minimo)
                    

def esci(voti):
    print("Sei uscito dalla gestione voti")

while True:
    print("Benvenuto sulla gestione voti, scegli una delle seguenti opzioni")
    print("1)Aggiungi studente")
    print("2)Visualizza i voti")
    print("3)Modifica voto")
    print("4)Elimina studente")
    print("5)Calcola media")
    print("6)Trova il voto massimo")
    print("7)Trova il voto minimo")
    print("8)Esci")
    scelta = int(input())
    while scelta<1 or scelta>8:
        print("Errore, puoi scegliere solamente una delle opzioni 1-5")
        scelta = int(input())
    if scelta == 1:
        aggiungi_studente(voti)
    elif scelta == 2:
        visualizza_voti(voti)
    elif scelta == 3:
        modifica_voto(voti)
    elif scelta == 4:
        elimina_studente(voti)
    elif scelta == 5:
        calcola_media(voti)
    elif scelta == 6:
        trova_massimo(voti)
    elif scelta == 7:
        trova_minimo(voti)
    elif scelta == 8:
        esci(voti)
        break



