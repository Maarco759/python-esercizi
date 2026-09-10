lista = []
nuova_lista = []
elementi = int(input("Quanti elementi vuoi inserire nella lista?? "))
for i in range(elementi):
    elemento = input("Inserisci un elemento: ")
    lista.append(elemento)
    
lista.sort()
print("La lista riordinata in ordine, è la seguente: ")
print(lista)
