lis_voti = []
def inserisci_voti(lis_voti):
    voti = int(input("Quanti voti vuoi inserire? "))
    for i in range(voti):
        voto = float(input("Inserisci il voto (1-10): "))
        while voti<1 or voti>10:
            print("Errore, puoi inserire solamente voti da 1 a 10")
            voto = float(input("Inserisci il voto: "))
        lis_voti.append(voto)

def media(lis_voti):
    if lis_voti == []:
        print("Nessun voto presente")
    else:
        somma_voti = 0
        media = 0.0
        for voto in lis_voti:
            somma_voti += voto
        media = somma_voti / len(lis_voti)
        print("La media dei voti inseriti è: "+str(media))

def massimo(lis_voti):
    if lis_voti == []:
        print("Nessun voto presente")
    else:
        mass = lis_voti[0]
        for voto in lis_voti:
            if voto>mass:
                mass=voto
        print("Il voto più alto è: "+str(mass))

def minimo(lis_voti):
    if lis_voti == []:
        print("Nessun voto presente")
    else:
        minimo = lis_voti[0]
        for voto in lis_voti:
            if voto<minimo:
                minimo=voto
        print("Il voto più basso è: "+str(minimo))

def esci():
    print("Sei uscito dalla gestione voti")

while True:
    print("Benvenuto sulla gestione voti, scegli una delle seguenti opzioni")
    print("1)Inserisci dei voti")
    print("2)Visualizza la media voti")
    print("3)Visualizza il voto più alto")
    print("4)Visualizza il voto più basso")
    print("5)Esci")
    scelt = int(input())
    while scelt<1 or scelt>5:
        print("Errore, puoi scegliere solamente una delle opzioni 1-5")
        scelt = int(input())
                    
    if scelt == 1:
        inserisci_voti(lis_voti)
    elif scelt == 2:
        media(lis_voti)
    elif scelt == 3:
        massimo(lis_voti)
    elif scelt == 4:
        minimo(lis_voti)
    elif scelt == 5:
        esci()
        break


