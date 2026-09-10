with open ("test_prova.txt","r") as file:
    nomi = file.readlines()
for nome in nomi:
    print(nome.strip())
