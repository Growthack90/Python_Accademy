"""Disegna un grafo con nodi casuali collegati tra loro"""
from turtle import *
from random import randint

def inizializza(titolo):
    """Inizializza la finestra del programma"""
    title(titolo)
    setup(size, size, 0, 0) # Dimensiona e posiziona la finestra principale
    shape("circle")         # Costume a forma (shape) di cerchio
    pensize(2)
    shapesize(2, 2, 1)      # Raddoppia il costume in larghezza e altezza
    color("grey", "orange") # Penna grigia (grey) e riempimento arancio (orange)

def disegna_nodi(n):
    """Disegna n nodi casuali all'interno del canvas"""
    stamp() # Lascia un impronta iniziale del costume corrente
    for i in range(n):
        # Spostamento massimo = metà dimensione meno una cornice di 20 px (pixel)
        delta_max = (size // 2) - 20   # Le parentesi non sono necessarie
        x = randint(-delta_max, delta_max)
        y = randint(-delta_max, delta_max)
        goto(x, y)
        stamp() # Lascia un impronta del costume corrente

if __name__ == "__main__":
    size = 800 # Altezza e larghezza della finestra uguali
    inizializza("Cerchi colorati casuali")
    disegna_nodi(8)
