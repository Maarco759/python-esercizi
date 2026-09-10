def aggiungi_oggetto(inventario):
    oggetto = input("Inserisci un oggetto: ")
    inventario.append(oggetto)
    print("Hai inserito: ",oggetto)

def visualizza_inventario(inventario):
    if inventario == []:
        print("Inventario vuoto")
    else:
        print("Eccco cosa possiedi nell'inventario: ") 
        for oggetto in inventario: 
            print("-"+oggetto)

def rimuovi_oggetto(inventario):
    if inventario == []:
                print("Inventario vuoto")
    else:
        print("Ecco cosa possiedi:")
        for i in range(len(inventario)):
            print(i+1, "-", inventario[i])
                    
        scelt = int(input("Quale oggetto vuoi rimuovere? "))
        while scelt < 1 or scelt > len(inventario):
            print("Scelta non valida")
            scelt = int(input())
                
        oggetto = inventario.pop(scelt-1)
        print("Hai rimosso:", oggetto)
inventario = []     
while True:
    print("Benvenuto nell'inventario, scegli una delle opzioni 1-3")
    print("Menù:")
    print("1)Visualizza inventario")
    print("2)Aggiungi un oggetto")
    print("3)Rimuovi un oggetto")
    scelta = int(input("Inserisci un'opzione: "))
    while scelta < 1 or scelta > 3:
        print("Errore, scelta non valida, reinserisci: ")
        scelta = int(input())
        
    if scelta == 1:
        visualizza_inventario(inventario)
    elif scelta == 2:
        aggiungi_oggetto(inventario)
    elif scelta == 3:
        rimuovi_oggetto(inventario)

            
