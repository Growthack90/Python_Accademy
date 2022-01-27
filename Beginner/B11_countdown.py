"""Utilizza un ciclo "for" per effettuare un conto alla rovescia che dura 10 secondi"""
import time

for i in range(10, 0, -1):
    print(i, end="...")
    time.sleep(1)

print("vai!")
