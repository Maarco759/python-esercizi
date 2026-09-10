lista = []
trovato = False
numeri = int(input("Quanti numeri vuoi inserire?? "))
for i in range(numeri):
    num = float(input("Inserisci il numero: "))
    lista.append(num)
    
scelta = float(input("Quale numero vuoi cercare?? "))
for numero in lista:
    if numero == scelta:
        trovato = True 
if trovato == True:
    print("Numero trovato")
else:
    print("Numero non trovato")

        
