"""Calcola l'area e il perimetro di un cerchio dato il suo raggio. Prima versione"""
import math

r = float(input("Raggio: "))

perimetro = 2 * math.pi * r
area = math.pi * r * r

print("Circonferenza:", round(perimetro, 2))
print("Area:", round(area, 2))
