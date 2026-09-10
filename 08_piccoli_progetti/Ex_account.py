#Indovinare la password
pass_corr = "1234"
cont = 0
accesso = False
#statistiche giocatore
livello = 1
esperienza = 0.0
monete = 100
inventario = []
#dizionario
prezzi = {
    "Spada": 50,
    "Armatura": 80,
    "Pozione": 20
}
while cont<3:
    pass_ins = input("Indovinare la password per accedere: ")
    if pass_corr == pass_ins:
        print("Accesso eseguito")
        accesso = True 
        break
    else:
        cont += 1
        print("Password errata, riprovare.")
        print("Ti sono rimasti "+str(3-cont)+" tentativi")
        if cont == 3:
            print("Account bloccato")
    
if accesso == True:
    while True: 
        print("Benvenuto del Menù dell'account, seleziona una di queste opzioni: ")
        print("1)Visualizza le statistiche del giocatore")
        print("2)Guadagna punti esperienza")
        print("3)Compra un oggetto")
        print("4)Visualizza inventario")
        print("5)Vendi un oggetto")
        print("6)Esci")
        scelta = int(input())
        while scelta<1 or scelta>5:
            print("Errore, scegli le opzioni 1-5")
            scelta = int(input("Reinserisci la tua scelta: "))
            break
                
        if scelta == 1:
            print("Hai: ")
            print("Livello: "+str(livello))
            print("Esperienza: "+str(esperienza))
            print("Monete: "+str(monete))
        elif scelta == 2:
            print("Quanti punti esperienza hai ottenuto? Inseriscila: ")
            esp = float(input())
            while esp <0:
                print("Errore, inerire esperienza positiva")
                esp = float(input())
                
            esperienza = esperienza + esp
            print("Ok, ora hai "+str(esperienza)+" punti esperienza")
            while esperienza >=1000:
                livello += 1
                esperienza -= 1000

            print("Sei salito al livello", livello)
        elif scelta == 3:
            spada = 50
            armatura = 80
            pozione = 20
            print("Scegli cosa comprare: ")
            print("1)spada = 50 ")
            print("2)armatura = 80")
            print("3)pozione = 20")
            scelt = int(input())
            while scelt<1 or scelt>3:
                print("Errore: puoi inserire una tra le opzioni 1-3")
                scelt = int(input())
            if scelt == 1:
                if monete >= spada:
                    print("Complimenti hai comprato una spada!")
                    inventario.append("Spada")
                    monete = monete - spada
                else:
                    print("Monete insufficienti")
            elif scelt == 2:
                if monete >= armatura:
                    print("Complimenti hai comprato un armatura!")
                    inventario.append("Armatura")
                    monete = monete - armatura
                else:
                    print("Monete insufficienti")
            elif scelt == 3:
                if monete >= pozione:
                    print("Complimenti hai comprato una pozione!")
                    inventario.append("Pozione")
                    monete = monete - pozione
                else:
                    print("Monete insufficienti")
        elif scelta == 4:
            if inventario == []:
                print("Inventario vuoto")
            else:
                print ("Eccco cosa possiedi nell'inventario: ") 
                for oggetto in inventario: 
                    print("-"+oggetto)
        elif scelta == 5:
            if inventario == []:
                print("Inventario vuoto")
            else:
                print("Ecco cosa possiedi:")
                for i in range(len(inventario)):
                    print(i+1, "-", inventario[i])
                    
                scelt = int(input("Quale oggetto vuoi vendere? "))
                while scelt < 1 or scelt > len(inventario):
                    print("Scelta non valida")
                    scelt = int(input())
                
                oggetto = inventario.pop(scelt-1)
                print("Hai venduto:", oggetto)
                monete += oggetto
        elif scelta == 6:
            print("Salvataggio eseguito")
            print("Arrivederci")
                
            
            
            
            
                
           

                        
            
            
            
            

                    
            
            
        
