stringa = input("Inserisci una stringa: ")
stringa_invert = ""
for i in range(len(stringa)-1,-1,-1):
    stringa_invert = stringa_invert + stringa[i]
print("La stringa invertita è: "+str(stringa_invert))
