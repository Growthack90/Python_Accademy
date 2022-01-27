"""Calcola l'ipotenusa note le misure dei cateti"""
import math    # Serve per la funzione sqrt()

a = eval(input("cateto 1: "))
b = eval(input("cateto 2: "))

i = math.sqrt(a*a + b*b)   # Ipotenusa in base al teorema di Pitagora
print("Ipotenusa:", i)
