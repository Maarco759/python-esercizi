#liste: le posizioni delle liste si iniziano a contare da 0 
alcolici = ["Vodka","Jagermaister","Gin"]
print(alcolici[0])
#contiamo quanti elementi ci sono nella lista grazie alla funzione len 
quantità_alcolici = len (alcolici)
print (quantità_alcolici)
#per aggiungere nuovi elementi alla fine di una lista utilizzo la funzione append 
alcolici.append("Quattro bianchi")
#per aggiungere nuovi elementi in qualsiasi posizione della lista si usa la funzione insert
alcolici.insert(2, "Martini")
#per eliminare un elemento dalla lista utilizzo la funzione remove
alcolici.remove("Vodka")
#per eliminare un elemento dalla lista con la sua posizione utilizzo la funzione pop
alcolici.pop(1)
print(alcolici)
alcolici.append("Vodka")
#per modificare un elemento della lista:
alcolici[2]="Caipiroska"
print(alcolici)
alcolici.append("Martini")
alcolici.append("Quattro bianchi")
print(alcolici)
#per riordinare gli elementi in ordine alfabetio utilizzo la funzione sort
alcolici.sort()
print(alcolici)
#per concatenare due liste utilizzo il + per concatenare 
alcolici = ["Vodka","Jagermaister","Gin"]
analcolici = ["Limonata", "Gazosa"]
menu_drink = alcolici+analcolici
print(menu_drink)
#verificare se un elemento è nella lista 
if "Vodka" in alcolici:
    print("La bevanda è in alcolici")
#stampare la lista senza virgolette
alcolici = ["Vodka","Jagermaister","Gin"]
print ("Eccco la lista di drink alcolici: ") 
print(alcolici[0])
print(alcolici[1])
print(alcolici[2])
#per evitare ripetizioni utilizziamo il ciclo for:
alcolici = ["Vodka","Jagermaister","Gin"]
print ("Eccco la lista di drink alcolici: ")
for alcolico in alcolici: #alcolico è una variabile di ciclo 
    print(alcolico)
#se voglio fermarmi a un determinato elemento 
alcolici = ["Vodka","Jagermaister","Gin"]
print ("Eccco la lista di drink alcolici: ")
for alcolico in alcolici: 
    if alcolico == "Jagermaister":
        break
    print(alcolico)
#se volessi continuare:
alcolici = ["Vodka","Jagermaister","Gin"]
print ("Eccco la lista di drink alcolici: ")
for alcolico in alcolici: 
    if alcolico == "Jagermaister":
        continue
    print(alcolico)
#utilizziamo il ciclo for con tutti gli elementi iterabili
#se volessi stampare ogni lettera
for lettera in "Marco":
    print(lettera)
for numero in range (1,19):
    print(numero)
#ciclo while
a = 1
while a<5:
    print(a)
    a += 1
    continue
#giochino
while True:
    print("Cosa fa un uccellino dentro un computer?")
    risposta = input()
    if risposta == "chip":
        print("Risposta esatta")
        break 
    else:
        print("Ritenta")
#si utilizza il %(modulo) per verificare il resto in una condizione
        
    
    

