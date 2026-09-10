studenti = {
    "studente1": {
        "nome": "Luca",
        "eta": 17,
        "voto": 8
    },
    "studente2": {
        "nome": "Marco",
        "eta": 18,
        "voto": 9
    },
    "studente3": {
        "nome": "Anna",
        "eta": 17,
        "voto": 6
    }
}
V = 0
S = 0
for studente in studenti:
    V += 1
    S = S + studenti[studente]["voto"]
m = S / V
print("La media dei voti è: ",m)
