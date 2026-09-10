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
for studente in studenti:
    if studenti[studente]["voto"] >= 8:
        print(studenti[studente]["nome"],"-",studenti[studente]["voto"])
