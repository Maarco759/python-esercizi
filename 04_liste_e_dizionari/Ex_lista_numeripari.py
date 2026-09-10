lista = []
contP = 0
numeri = int(input("Quanti numeri vuoi inserire?? "))
for i in range(numeri):
    num = int(input("Inserire il numero: "))
    lista.append(num)
    pari = lista[0]
for num in lista:
    if num%2==0:
        contP += 1
print("I numeri nella lista sono: ")
print(lista)
print("I numeri pari della lista sono: "+str(contP))
