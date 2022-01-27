"""Calcola l'area di un triangolo fornendo le misure dei suoi lati
in base alla formula di Erone"""
import math

lato1 = eval(input("Lato 1: "))
lato2 = eval(input("Lato 2: "))
lato3 = eval(input("Lato 3: "))

if lato1 < lato2 + lato3 and lato2 < lato1 + lato3  and lato3 < lato1 + lato2:
    p = (lato1 + lato2 + lato3) / 2 # Semiperimetro
    a = p - lato1
    b = p - lato2
    c = p - lato3
    area = math.sqrt(p * a * b * c)
    print("Area:", area)
else:
    print("Misure non valide per un triangolo")
