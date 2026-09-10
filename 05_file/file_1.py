with open("test_prova.txt","a") as file:
    file.write("\nPaolo")

with open("test_prova.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)
