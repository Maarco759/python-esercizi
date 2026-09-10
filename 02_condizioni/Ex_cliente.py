prezzo_drink = 5.5
sconto = 1
cliente_preferito = "Giacomino"
prezzo_scontato = prezzo_drink-sconto
print ("Salve, come ti chiami?")
nome_cliente = input()
print ("Ok "+str(nome_cliente)+", quanti anni hai?")
anni_cliente = int(input())
if nome_cliente == cliente_preferito and anni_cliente > 25:
    print("Il prezzo del tuo drink è di: "+str(prezzo_scontato))
else:
    print("Il prezzo del tuo drink è di: "+str(prezzo_drink))

