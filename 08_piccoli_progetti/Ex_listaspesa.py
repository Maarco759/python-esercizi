prodotti = int(input("Quanti prodotti vuoi acquistare? "))
lista_spesa =[]
for i in range(prodotti):
    elemento = input("Inserisci un prodotto: ")
    lista_spesa.append(elemento)
    
print("La tua lista della spesa è la seguente: ")
for elemento in lista_spesa:
    print("-",elemento)
while True:
    print("Menù: ")
    print("1)Aggiungere un prodotto: ")
    print("2)Visulizzare la lista: ")
    print("3)Rimuovere un prodotto: ")
    print("4)Uscire")
    scelta = int(input("Scegli cosa fare: "))
    while scelta<1 or scelta>4:
        print("Errore, inserire una delle opzioni 1-4: ")
        scelta = int(input("Scegli cosa fare: "))
    if scelta == 1:
        elemento = input("Inserisci un prodotto: ")
        lista_spesa.append(elemento)
    elif scelta == 2:
        if lista_spesa == []:
            print("Lista della spesa vuota")
        else:
            print("La tua lista della spesa è la seguente: ")
            for elemento in lista_spesa:
                print("-",elemento)
    elif scelta == 3:
            if lista_spesa == []:
                print("Lista della spesa vuota")
            else:
                print("Ecco cosa possiedi nella lista della spesa: ")
                for i in range(len(lista_spesa)):
                    print(i+1, "-", lista_spesa[i])
                scelt = int(input("Quale elemento vuoi rimuovere dalla lista? "))
                while scelt < 1 or scelt > len(lista_spesa):
                    print("Scelta non valida")
                    scelt = int(input())
                
                oggetto = lista_spesa.pop(scelt-1)
                print("Hai rimosso:", oggetto)
    elif scelta == 4:
        print("Sei uscito dal menù spesa")
        break
        
