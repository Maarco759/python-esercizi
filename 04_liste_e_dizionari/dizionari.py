#dizionari: coppie di vaori: chiave-valore 
mio_dict = {"mia_chiave": "mio_valore"}
#aggiornare una chiave
mio_dict["mia_chiave"] = "mio valore aggiornato"
print(mio_dict["mia_chiave"])
#aggiungere una nuova chiave
mio_dict["nuova chiave"] = "nuovo valore"
print(mio_dict)
#verificarec se una chiave è nel dizionario
"spam" in mio_dict
"mia_chiave" in mio_dict
#rimuovere un elemento in un dizionario
del mio_dict["mia_chiave"]
print(mio_dict)
#visualizzare le chiavi
print(mio_dict.keys())
#visualizzare i valori
print(mio_dict.values())
#visualizzare le coppie chiave-valore
print(mio_dict.items())
#visualizzare chiavi, oggetti e coppie 
items = mio_dict.items()
print(type(items))
print(list(items))
#nei cicli
for chiave in mio_dict.keys():
    print(chiave)
#metodo get per verificare che una chiave non è nel dizionario
print(mio_dict.get("spam", "chiave non trovata"))
#metodo setdefault per verificare qualora non ci fosse una chiave assegnata di aggiungerne una di default 
print(mio_dict.setdefault("birra", "beer"))
print(mio_dict)
print(mio_dict.setdefault("nuova chiave", "ciao")) #nel dizionario il valore non si modifica 


