"""Aristide invita a una festa n amici.
Ogni invitato che arriva stringe la mano di coloro che sono già presenti.
Quante sono in totale le strette di mano?"""
n = eval(input("Numero di invitati: "))
# partecipanti = n + 1 # C'è anche Aristide
strette = 0
i = 1

while i < n:
    strette += i
    print("Strette di mano: ", strette)
    i = i + 1

print("Strette di mano: ", strette)
