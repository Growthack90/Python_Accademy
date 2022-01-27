"""Trova le soluzioni di un'equazione di secondo grado
Ipotesi: le soluzioni sono numeri interi appartenenti all'intervallo [inf, sup]"""
a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))

inf, sup = -1000, 1000 # Estremo inferiore e superiore con assegnazione multipla

for x in range(inf, sup + 1):
    y = a*x*x + b*x + c
    # print(x, y) # Stampa tutti i valori della coppia (x, y) al variare di x
    
    if y == 0:
        print("Soluzione:", x)
        
'''
Per provare i vari casi possibili esegui il programma con i valori: 1, -2, 0 poi con 1, 0, 0 e, infine, con 1, -2, 2.
'''
