try:
    numero = int(input("Inserisci un numero: "))
    risultato = 10 / numero
    print("Risultato:", risultato)
except ValueError:
    print("Devi inserire un numero")

except ZeroDivisionError:
    print("Non puoi dividere per zero")
else:
    print("Hai inserito correttamente: ",numero)
finally:
    print("Programma terminato")
