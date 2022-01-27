"""Trova le soluzioni di un'equazione di secondo grado"""
import math    # Serve per la funzione sqrt()

a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))

delta = b*b - 4*a*c # Per maggiore leggibilità non usiamo spazi nelle moltiplicazioni

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x1 = -b / (2*a)
    print("x1 = x2 =", x1)
else:
    print("Impossibile, delta < 0")

'''
Per provare i vari casi possibili esegui il programma con i valori: 
1, 2, 4 poi con 1, 0, 0 e, infine, con 1, -2, 2.
'''
