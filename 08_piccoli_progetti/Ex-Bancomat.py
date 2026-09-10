pin_corretto = 677
cont = 0
accesso = False
while cont<3:
    pin = int(input("Inserisci il PIN corretto "))
    if pin == pin_corretto:
        print("Accesso consentito al Bancomat")
        accesso = True 
        break
    else:
        cont += 1
        print("PIN errato, ti rimangono: "+str(3-cont)+" tentativi")

if accesso:
    saldo = float(input("Benvenuto nel Bancomat, inserisci il tuo saldo in euro: "))
    while True:
        print("Menu: ")
        print("1) visualizzare il saldo")
        print("2) depositare denaro")
        print("3) prelevare denaro")
        print("4) uscire dal bancomat")
        print("Cosa vuoi fare?")
        scelta = int(input())
        while scelta < 1 or scelta > 4:
            print("Scelta non valida")
            scelta = int(input("Riprova: "))
        if scelta == 1:
            print("Il tuo saldo è di: " + str(saldo) + " euro")
        elif scelta == 2:
            depo = float(input("Inserire quanto si vuole depositare: "))
            while depo<=0:
                print("Errore, inserire importi positivi")
                depo = float(input("Inserire quanto si vuole depositare: "))
                
            saldo = saldo + depo
            print("Ora il tuo saldo è di: " + str(saldo) + " euro")
        elif scelta == 3:
            prelev = float(input("Inserire quanto si vuole prelevare: "))
            if prelev > saldo:
                print("Saldo insufficiente")
            else:
                saldo = saldo - prelev
                print("Ora il tuo saldo è di: " + str(saldo) + " euro")
        elif scelta == 4:
            print("Sei uscito dal Bancomat.")
            break      
            
                           
            
