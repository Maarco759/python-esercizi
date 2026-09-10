with open("test_prova.txt","r") as file:
    nomi = file.readlines()
    for nome in nomi:
        if len(nome.strip())>4:
            print(nome.strip())
