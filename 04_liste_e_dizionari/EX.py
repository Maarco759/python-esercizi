lista = []
numeri = int(input("Quanti numeri vuoi inserire?? ")) 
for i in range(numeri):
    num = float(input("Inserisci un numero: "))
    lista.append(num)
mass = lista[0]
for num in lista:
        if num>mass:
            mass=num
print("Il numero più grande è: " +str(mass))
    
   
        
    
        
    

