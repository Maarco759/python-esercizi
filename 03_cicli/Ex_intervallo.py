inizio = int(input("Inserisci il numero iniziale: "))
fine = int(input("Inserisci il numero finale: "))
numero = inizio
print("I numeri pari compresi tra i due numeri sono: ")
while numero <= fine:
    if numero % 2 == 0:
        print(numero)

    numero += 1
        
