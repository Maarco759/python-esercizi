def trova_massimo(lista):
    mass = lista[0]
    for num in lista:
        if num>mass:
            mass=num
    return mass

lista = []
numeri = int(input("Quanti numeri vuoi inserire?? "))
for i in range(numeri):
    num = float(input("Inserisci il numero: "))
    lista.append(num)

mass = trova_massimo(lista)
print("Il massimo della lista di numeri inseriti: "+str(mass))
