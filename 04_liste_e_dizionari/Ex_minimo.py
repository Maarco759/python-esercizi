lista = []
numeri = int(input("Quanti numeri vuoi inserire?? "))
for i in range(numeri):
    num = float(input("Inserisci il numero: "))
    lista.append(num)
minim = lista[0]
for num in lista:
    if num<minim:
        minim=num
print("Il numero più piccolo è: "+str(minim))
