lista = []
def aggiungi_attività(lista):
    attività = input("Inserisci un'attività: ")
    lista.append(attività)
    print("Hai inserito: ",attività)
    
def visualizza_attività(lista):
    if lista == []:
        print("Lista attività vuota")
    else:
        print("Eccco la tua lista delle attività: ") 
        for attività in lista: 
            print("-"+attività)
            
def rimuovi_attività(lista):
    if lista == []:
        print("Lista attività vuota")
    else:
        print("Ecco la tua lista delle attività: ")
        for i in range(len(lista)):
            print(i+1, "-", lista[i])
                    
        scelt = int(input("Quale attività vuoi rimuovere? "))
        while scelt < 1 or scelt > len(lista):
            print("Scelta non valida")
            scelt = int(input())
                
        att = lista.pop(scelt-1)
        print("Hai rimosso:", att)

def segn_complet(lista):
    if lista == []:
        print("Non hai alcun attivià da segnare come completata")
    else:
        print("Ecco le attività che puoi segnare come completate")
        for i in range(len(lista)):
            print(i+1,"-",lista[i])
            
        az = int(input("Inserisci quale attività vuoi segnare come completata: "))
        while az<1 or az>len(lista):
            print("Scelta non valida, reinserisci")
            az = int(input())
            
        if lista[az-1].startswith("✓"):
            print("L'attività è già segnata come completata")
        else:
            lista[az-1] = "✓ " + lista[az-1]
            print("Attività segnata come completata")
            
def cerca_attività(lista):
    trovato = False
    q = input("Quale attività vuoi cercare?? ")
    q = q.lower()
    if lista == []:
        print("Non è presente alcuna attività da cercare")
    else:
        for attivita in lista:
            attivita = attivita.lstrip("✓ ")
            attivita = attivita.lower()
            if attivita == q:
                trovato = True
            if trovato ==  True:
                print("L'attività è nella to-do list")
            else:
                print("L'attività non è nella to-do list")
                
def lun_attività(lista):
    lunghezza_lista = len(lista)
    print("Nella to-do list ci sono: "+str(lunghezza_lista)+" attività")

def svuota_lista(lista):
    if lista == []:
        print("La lista è già vuota")
    else:
        lista.clear()
        print("Hai rimosso tutte le tue attività")

def esci_lista(lista):
    print("Sei uscito dalla lista")
    
while True:
    print("1) Aggiungere un'attività")
    print("2) Visualizzare le attività")
    print("3) Rimuovere un'attività")
    print("4) Segnare un'attività come completata")
    print("5) Cercare un'attività")
    print("6) Contare quante attività ci sono")
    print("7) Svuotare tutta la lista")
    print("8) Uscire")
    scelta = int(input("Seleziona una di queste 8 opzioni: "))
    while scelta<1 or scelta>8:
        scelta = int(input("Errore, puoi selezionare solo una di queste 8 opzioni: "))
    if scelta == 1:
        aggiungi_attività(lista)
    elif scelta == 2:
        visualizza_attività(lista)
    elif scelta == 3:
        rimuovi_attività(lista)
    elif scelta == 4:
        segn_complet(lista)
    elif scelta == 5:
        cerca_attività(lista)
    elif scelta == 6:
        lun_attività(lista)
    elif scelta == 7:
        svuota_lista(lista)
    elif scelta == 8:
        esci_lista(lista)
        break

    




        
       
