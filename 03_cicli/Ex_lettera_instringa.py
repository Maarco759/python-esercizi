stringa = input("Inserisci una stringa: ")
contL = 0
scelta = input("Inserisci quale lettera vuoi contare: ")
for lettera in stringa:
    if lettera == scelta:
        contL += 1
print("La lettera scelta è presente nella stringa: "+str(contL)+" volte.")


