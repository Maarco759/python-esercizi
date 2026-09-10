nuova_frase = ""
frase = input("Inserisci una frase: ")
for carattere in frase:
    if carattere != " ":
        nuova_frase = nuova_frase + carattere 
print("La nuova frase senza spazi è: "+nuova_frase) 
