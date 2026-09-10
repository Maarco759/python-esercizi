#funzioni: servono per sintetizzare delle righe di codice
#il parametro è la variabile generica che utiliziamo nella definizione di funzione 
#l'argomento è ciò che viene nserito quando viene inviato il programma
def fai_la_pasta(tipo_pasta):
    print("Prendi la pentola")
    print("Metti l'acqua")
    print("Fai bollire")
    print("Prepara il sugo")
    print("Impiatta e metti "+tipo_pasta)
fai_la_pasta("spaghetti")

#parametri di default
def fai_la_pasta(tipo_pasta, metti_sugo):
    print("Prendi la pentola")
    print("Metti l'acqua")
    print("Fai bollire")
    print("Prepara il sugo")
    print("Impiatta e metti "+tipo_pasta)
    if metti_sugo:
        print("prepara il sugo")
fai_la_pasta("spaghetti", True)

#parametri di default
def nuovo_laptop(ram, cpu, antivirus=False):
    print("Il nuovo computer ha le seguenti caratteristiche: ")
    print("RAM: "+ram)
    print("CPU: "+cpu)
    if antivirus:
        print("Hai comprato anche l'antivirus!!")
nuovo_laptop("16GB","i7", True)

#return
def addizione(a,b):
    risultato = a + b
    return risultato
risultato = addizione(13, 17)
print(risultato)    

    



