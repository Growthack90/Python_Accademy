"""Calcola l'area e il perimetro di un cerchio dato il suo raggio.
Seconda versione con gestione dell'errore di inserimento"""
import math

try:
    r = float(input("Raggio: "))

    perimetro = 2 * math.pi * r
    area = math.pi * r * r

    print("Circonferenza:", round(perimetro, 2))
    print("Area:", round(area, 2))
except:
    print("Valore inserito non valido!")
