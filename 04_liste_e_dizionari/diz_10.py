spese = {}
def aggiungi_spese(spese):
    categorie = int(input("Quanti spese vuoi inserire?? "))
    for i in range(categorie):
        categoria = input("Inserisci la tua spesa: ")
        spese[categoria] = float(input("Inserisci l'ammontare della spesa: "))

def visualizza_spese(spese):
    if spese == {}:
        print("Registro spese vuoto")
    else:
        print("Ecco le tue spese: ")
        for prodotto, quantita in spese.items():
            print(prodotto,"-",quantita," euro")

def modifica_spesa(spese):
    if spese == {}:
        print("Registro spese vuoto, non puoi modificare alcuna spesa")
    else:
        print("Ecco le tue spese: ")
        spese_tot = list(spese.keys())
        for i in range(len(spese_tot)):
            print(i+1,"-",spese_tot[i]," euro")
        sc = int(input("Seleziona quale spesa vuoi modificare: "))
        while sc < 1 or sc > len(spese):
           sc = int(input("Scelta non valida, reinserisci: "))
        mod_spesa = spese_tot[sc-1]
        spese[mod_spesa] = float(input("Inserisci il nuovo ammontare della spesa: "))

def rimuovi_spesa(spese):
    if spese == {}:
        print("Registro spese vuoto")
    else:
        print("Ecco le tue spese: ")
        spese_tot = list(spese.keys())
        for i in range(len(spese_tot)):
            print(i+1,"-",spese_tot[i]," euro")
        scelt = int(input("Quale spesa vuoi eliminare?? "))
        while scelt < 1 or scelt > len(spese):
            scelt = int(input("Scelta non valida, reinserisci: "))
        spesa = spese_tot[scelt-1]
        ammontare = spese.pop(spesa)
        print("Hai rimosso: ",spesa,"-",ammontare," euro")

def cerca_spese(spese):
    trovato = False
    cerca = input("Quale spesa vuoi cercare? ")
    for spesa in spese:
        if cerca.lower() in spesa.lower():
            trovato = True
    if trovato == True:
        print("La spesa è presente nel registro")
    else:
        print("La spesa non è presente nel registro")

def totale_spese(spese):
    totale = 0
    for quantita in spese.values():
        totale += quantita  
    print("La tua spesa totale generale è di: ",totale," euro")
    
def spesa_massima(spese):
    lista_spese = list(spese.values())
    massimo = lista_spese[0]
    for quantita in spese.values():
        if quantita > massimo:
            massimo = quantita 
    print("La tua spesa massima è di: ",massimo," euro")

def esci(spese):
    print("Sei uscito dal registro spese")

while True:
    print("Benvenuto nella tuo registro spese, seleziona una di queste opzioni: ")
    print("1)Visualizza le tue spese")
    print("2)Aggiungi nuove spese")
    print("3)Rimuovi spesa")
    print("4)Cerca spesa")
    print("5)Modifica una spesa")
    print("6)Calcolare il totale speso")
    print("7)Trovare la spesa più alta")
    print("8)Uscire")
    scelta = int(input("Scegli una delle opzioni 1-8: "))
    if scelta == 1:
        visualizza_spese(spese)
    elif scelta == 2:
        aggiungi_spese(spese)
    elif scelta == 3:
        rimuovi_spesa(spese)
    elif scelta == 4:
        cerca_spese(spese)
    elif scelta == 5:
        modifica_spesa(spese)
    elif scelta == 6:
        totale_spese(spese)
    elif scelta == 7:
        spesa_massima(spese)
    elif scelta == 8: 
        esci(spese)
        break

          
        
    

