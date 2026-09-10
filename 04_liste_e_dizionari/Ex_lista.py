lista =[]
s=0
numeri = int(input("Quanti numeri vuoi inserire?? "))
for i in range(numeri):
    print("Inserisci il numero: ")
    num = float(input())
    lista.append(num)
    s=s+num
print(lista)
print("La somma dei numeri inseriti nella lista è di: "+str(s))
    


