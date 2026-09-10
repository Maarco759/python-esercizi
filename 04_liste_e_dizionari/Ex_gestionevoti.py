voti = int(input("Quanti voti vuoi inserire?? "))
vot = []
s = 0
m = 0.0
for i in range(voti):
    voto = float(input("Inserisci il voto: "))
    while voto<0 or voto>10:
        print("Puoi inserire solamente voti da 1 a 10")
        voto = float(input("Inserisci il voto: "))
        
    vot.append(voto)
    s = s + voto
    m = s/voti
print("La tua media dei voti è: "+str(m))

mass = vot[0]
for voto in vot:
    if voto>mass:
        mass=voto
print("Il voto più alto è: "+str(mass))

mini = vot[0]
for num in vot:
    if num<mini:
        mini=num
print("Il voto più basso è: "+str(mini))
print("L'esito del tuo anno è: ")
if m>=6:
    print("Promosso")
else:
    print("Bocciato")
    
        
