primo_est = int(input("Inserisci il primo estremo: "))
secondo_est = int(input("Inserisci il secondo estremo: "))
numero = primo_est
print("I numeri multipli di 5 compresi tra i due etremi sono: ")
while numero<=secondo_est:
    if numero%5==0:
        print(numero)
    numero += 1
