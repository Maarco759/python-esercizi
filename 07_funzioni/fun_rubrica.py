rubrica = {}
def vis_rubrica(rubrica):
    if rubrica == {}:
        print("Rubrica vuota")
    else:
        print("Ecco i contatti della rubrica: ")
        for contatto, numero in rubrica.items():
            print(contatto,"-",numero)

def aggiungi_contatti(rubrica):
    contatti = int(input("Quanti contatti vuoi inserire?? "))
    for i in range(contatti):
        contatto = input("Inserisci il nome il contatto: ")
        rubrica[contatto] = int(input("Inserisci il numero del contatto: "))
    
def rimuovi_contatto(rubrica):
    if rubrica == {}:
        print("Rubrica già vuota")
    else:
        print("Ecco i contatti della rubrica: ")
        chiavi = list(rubrica.keys())
        for i in range(len(chiavi)):
            print(i+1,"-",chiavi[i])
        scelt = int(input("Quale contatto vuoi eliminare?? "))
        while scelt < 1 or scelt > len(rubrica):
            scelt = int(input("Scelta non valida, reinserisci: "))
        nome_contatto = chiavi[scelt-1]
        numero = rubrica.pop(nome_contatto)
        print("Hai rimosso: ",nome_contatto,"-",numero)
        
def cerca_contatto(rubrica):
    trovato = False
    cerca = input("Quale contatto vuoi ceracare? ")
    for contatto in rubrica:
        if cerca.lower() in contatto.lower():
            trovato = True
    if trovato == True:
        print("Il contatto è nella rubrica")
    else:
        print("Il contatto non è nella rubrica")

def modifica_numero(rubrica):
    if rubrica == {}:
        print("Rubrica vuota, non puoi modificare nesssun numero")
    else:
        print("Ecco i contatti della rubrica: ")
        chiavi = list(rubrica.keys())
        for i in range(len(chiavi)):
            print(i+1,"-",chiavi[i])
        sc = int(input("Seleziona quale contatto vuoi modificare: "))
        while sc < 1 or sc > len(rubrica):
           sc = int(input("Scelta non valida, reinserisci: "))
        mod_numero = chiavi[sc-1]
        rubrica[mod_numero] = int(input("Inserisci il nuovo numero: "))

def esci():
    print("Sei uscito dalla rubrica")

while True:
    print("Benvenuto nella tua rubrica, seleziona una di queste opzioni: ")
    print("1)Visualizza la rubrica")
    print("2)Aggiungi nuovi contatti")
    print("3)Rimuovi contatto")
    print("4)Cerca contatto")
    print("5)Modifica numero")
    print("6)Uscire")
    scelta = int(input("Scegli una delle opzioni 1-5: "))
    if scelta == 1:
        vis_rubrica(rubrica)
    elif scelta == 2:
        aggiungi_contatti(rubrica)
    elif scelta == 3:
        rimuovi_contatto(rubrica)
    elif scelta == 4:
        cerca_contatto(rubrica)
    elif scelta == 5:
        modifica_numero(rubrica)
    elif scelta == 6: 
        esci()
        break


    
