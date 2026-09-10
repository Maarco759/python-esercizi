rubrica = []
while True:
    print("Benvenuto nella tua rubrica, seleziona una di queste opzioni: ")
    print("1)Visualizza la rubrica")
    print("2)Aggiungi nuovi contatti")
    print("3)Rimuovi contatto")
    print("4)Uscire")
    scelta = int(input("Scegli una delle opzioni 1-5: "))
    if scelta == 1:
        if rubrica == []:
            print("Rubrica vuota")
        else:
            print("Ecco i contatti della rubrica: ")
            for contatto in rubrica:
                print("-",contatto)
    elif scelta == 2:
        contatti = int(input("Quanti contatti vuoi inserire?? " ))
        for i in range(contatti):
            contatto = input("Inserisci il nome il contatto: ")
            rubrica.append(contatto)
    elif scelta == 3:
            if rubrica == []:
                print("Rubrica vuota")
            else:
                print("Ecco i contatti della rubrica: ")
                for i in range(len(rubrica)):
                    print(i+1, "-", rubrica[i])
                scelt = int(input("Quale contatto vuoi rimuovere dalla rubrica? "))
                while scelt < 1 or scelt > len(rubrica):
                    print("Scelta non valida")
                    scelt = int(input())
                
                persona = rubrica.pop(scelt-1)
                print("Hai rimosso:", persona)
    elif scelta == 4:
        print("Sei uscito dalla rubrica")
        break
        
                
        
