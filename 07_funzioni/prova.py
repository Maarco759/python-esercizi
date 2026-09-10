voti = {}
def aggiungi_studente(voti):
    nome_studente = input("Inserisci il nome dello studente:  ")
    voto_studente = float(input("Inserisci un voto (1-10) allo studente: "))
    voti[nome_studente] = voto_studente
aggiungi_studente(voti)
