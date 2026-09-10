contV = 0
parola = input("Inserisci una parola: ")
for lettera in parola:
    if lettera == "a" or lettera == "A":
        contV += 1
    elif lettera == "e" or lettera == "E":
        contV += 1
    elif lettera == "i" or lettera == "I":
        contV += 1
    elif lettera == "o" or lettera == "O":
        contV += 1
    elif lettera == "u" or lettera == "U":
        contV += 1
print("Le vocali minuscole che ci sono nella parola sono: "+str(contV))
    

