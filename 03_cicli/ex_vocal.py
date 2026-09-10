contV = 0
parola = input("Inserisci una parola: ")
for lettera in parola:
    if lettera == "a":
        contV += 1
    elif lettera == "e":
        contV += 1
    elif lettera == "i":
        contV += 1
    elif lettera == "o":
        contV += 1
    elif lettera == "u":
        contV += 1
print("Le vocali minuscole che ci sono nella parola sono: "+str(contV))
    

