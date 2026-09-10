lista = []
elementi = int(input("Quanti numeri vuoi inserire?? "))
for i in range(elementi):
    elemento = int(input("Inserisci il numero: "))
    lista.append(elemento)
for i in range(elementi-1,-1,-1):
    print(lista[i])
