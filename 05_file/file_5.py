with open("studenti.txt","r") as file:
    nomi = file.readlines()
    contS = 0
    for nome in nomi:
        contS += 1
    print("Gli studenti sono: ",contS)
        
