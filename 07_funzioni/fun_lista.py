def somma_lista(lista):
    s = 0
    for numero in lista:
        s = s + numero
    return s
numeri = [109,4,6]
risultato = somma_lista(numeri)
print(risultato)
