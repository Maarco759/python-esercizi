parola = input("Inserisci una parola: ")
palindroma = False
invertita = ""
for i in range(len(parola)-1,-1,-1):
    invertita = invertita + parola[i]
    
if parola == invertita:
    palindroma = True
if palindroma == True:
    print("La parola è palindroma")
else:
    print("La parola non è palindroma")

