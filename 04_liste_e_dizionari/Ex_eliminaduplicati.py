lista = []
nuova_lista = []
elementi = int(input("Quanti elementi vuoi inserire nella lista?? "))
for i in range(elementi):
    elemento = input("Inserisci un elemento: ")
    lista.append(elemento)
    
for element in lista:
    if element not in nuova_lista:
        nuova_lista.append(element)
print("La lista senza duplicati è la seguente: ")
for el in nuova_lista:
    print(el)
            
        
    
    
