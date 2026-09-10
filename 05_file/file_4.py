with open("studenti.txt","r") as file:
    nomi = file.readlines()
    for nome in nomi:
        if len(nome.strip())>5:
            print(nome.strip())
    
