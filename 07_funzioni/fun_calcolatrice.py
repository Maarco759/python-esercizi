def addizione(a,b):
    return a + b

def sottrazione(a,b):
    return a - b

def moltiplicazione(a,b):
    return a*b

def divisione(a,b):
    return a/b


while True:
    print("Menù: ")
    print("1)Addizione")
    print("2)Sottrazione")
    print("3)Moltiplicazione")
    print("4)Divisione")
    print("5)Esci")
    a = float(input("Inserisci il primo estremo dell'operazione: "))
    b = float(input("Inserisci il secondo estremo dell'operazione: "))             
    scelta = int(input("Scegli una delle seguenti operazioni 1-4:"))
    while scelta < 1 or scelta > 5:
        scelta = int(input("Errore, scegli una delle seguenti operazioni 1-4:"))
        
    if scelta == 1:
        risultato = addizione(a,b)
        print("Il risultato dell'addizione è: "+str(risultato))
    elif scelta == 2:
        risultato = sottrazione(a,b)
        print("Il risultato della sottrazione è: "+str(risultato))
    elif scelta == 3:
        risultato = moltiplicazione(a,b)
        print("Il risultato della moltiplicazione è: "+str(risultato))
    elif scelta == 4:
        risultato = divisione(a,b)
        print("Il risultato della divisione è: "+str(risultato))
    elif scelta == 5:
        print("Sei uscito dalla calcolatrice")
        break
        
