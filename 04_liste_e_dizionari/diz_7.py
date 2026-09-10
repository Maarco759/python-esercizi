persona = {"nome": "Marco", "eta": 17, "citta": "Potenza"}

inf = input("Quale informazione vuoi cercare?? ")

if inf in persona:
    print("La chiave esiste")
    print("Valore:", persona[inf])
else:
    print("La chiave non esiste")
