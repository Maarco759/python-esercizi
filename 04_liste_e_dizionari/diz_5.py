persona = {"nome": "Marco", "eta": 17, "citta": "Potenza"}
print("Ecco le chivi del dizionario")
for chiave in persona.keys():
    print(chiave)
del persona[input("Elimina una chiave: ")]
print(persona)
