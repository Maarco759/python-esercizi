persona = {}
persona["nome"] =  input("Inseriasci il tuo nome: ")
persona["eta"] = input("Inserisci la tua età: ") 
persona["citta"] = input("Inserisci la tua città: ")
print(persona)
for chiave, valore in persona.items():
    print(chiave, "=", valore)
