diz_parole = {}
frase = input("Inserisci una frase: ")
parole = frase.split()
for parola in parole:   
    if parola in diz_parole:
        diz_parole[parola] = diz_parole[parola] + 1
    else:
        diz_parole[parola] = 1

print(diz_parole)
        


