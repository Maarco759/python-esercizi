inventario = {}
def aggiungi_prodotti(inventario):
    prodotti = int(input("Quante prodotti vuoi inserire?? "))
    for i in range(prodotti):
        prodotto = input("Inserisci la prodotto: ")
        inventario[prodotto] = float(input("Inserisci la quantità: "))

def visualizza_prodotti(inventario):
    if inventario == {}:
        print("Inventario vuoto")
    else:
        print("Ecco i prodotti del tuo inventario: ")
        for prodotto, quantita in inventario.items():
            print(prodotto,"-",quantita)

def modifica_quantita(inventario):
    if inventario == {}:
        print("Inventario vuoto, non puoi modificare nesssun prodotto")
    else:
        print("Ecco i prodotti del tuo inventario: ")
        prodotti = list(inventario.keys())
        for i in range(len(prodotti)):
            print(i+1,"-",prodotti[i])
        sc = int(input("Seleziona quale prodotto vuoi modificare: "))
        while sc < 1 or sc > len(inventario):
           sc = int(input("Scelta non valida, reinserisci: "))
        mod_prodotto = prodotti[sc-1]
        inventario[mod_prodotto] = int(input("Inserisci nuova la quantità: "))

def rimuovi_prodotto(inventario):
    if inventario == {}:
        print("Inventario vuoto")
    else:
        print("Ecco i prodotti del tuo inventario: ")
        prodotti = list(inventario.keys())
        for i in range(len(prodotti)):
            print(i+1,"-",prodotti[i])
        scelt = int(input("Quale prodotto vuoi eliminare?? "))
        while scelt < 1 or scelt > len(inventario):
            scelt = int(input("Scelta non valida, reinserisci: "))
        nome_prodotto = prodotti[scelt-1]
        quantita = inventario.pop(nome_prodotto)
        print("Hai rimosso: ",nome_prodotto,"-",quantita)

def cerca_prodotto(inventario):
    trovato = False
    cerca = input("Quale prodotto vuoi ceracare? ")
    for prodotto in inventario:
        if cerca.lower() in prodotto.lower():
            trovato = True
    if trovato == True:
        print("Il prodotto è nel tuo inventario")
    else:
        print("Il prodotto non è nel tuo inventario")

def totale_prodotti(inventario):
    totale = 0
    for quantita in inventario.values():
        totale += quantita  
    print("Il numero totale dei prodotti nel tuo inventario è di: ",totale)
    
def prodotto_massimo(inventario):
    lista_prodotti = list(inventario.values())
    massimo = lista_prodotti[0]
    for quantita in inventario.values():
        if quantita > massimo:
            massimo = quantita 
    print("Il prodotto con massima quantità è: ",massimo)

def esci(inventario):
    print("Sei uscito dall'inventario del negozio")

while True:
    print("Benvenuto nella tuo inventario negozio, seleziona una di queste opzioni: ")
    print("1)Visualizza l'inventario")
    print("2)Aggiungi nuovi prodotti")
    print("3)Rimuovi prodotto")
    print("4)Cerca prodotto")
    print("5)Modifica quantità")
    print("6)Totale prodotti")
    print("7)Mostrare prodotto con quantità massima")
    print("8)Uscire")
    scelta = int(input("Scegli una delle opzioni 1-8: "))
    if scelta == 1:
        visualizza_prodotti(inventario)
    elif scelta == 2:
        aggiungi_prodotti(inventario)
    elif scelta == 3:
        rimuovi_prodotto(inventario)
    elif scelta == 4:
        cerca_prodotto(inventario)
    elif scelta == 5:
        modifica_quantita(inventario)
    elif scelta == 6:
        totale_prodotti(inventario)
    elif scelta == 7:
        prodotto_massimo(inventario)
    elif scelta == 8: 
        esci(inventario)
        break
