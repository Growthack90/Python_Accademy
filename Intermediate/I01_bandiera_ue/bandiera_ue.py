"""Disegna la bandiera dell'Unione Europea"""
import turtle

costume = "stella.gif"    # File che contiene l'immagine di una stella gialla

# Screen
screen = turtle.Screen()         # Crea un riferimento alla finestra di disegno
screen.bgcolor("blue4")          # Imposta il colore di sfondo del canvas
screen.addshape(costume)    # Registra un nuovo costume ("shape") 
screen.title("Bandiera dell'Unione Europea")
passi = screen.numinput("Dimensione in pixel", "Dimensione:")  # Finestra di input

# Turtle
ninja = turtle.Turtle()
ninja.up()                           # Non disegna sullo schermo
ninja.shape(costume)        # Indossa il nuovo costume
ninja.speed(1)                    # Velocità dell'animazione

n = 12      # Numero di stelle
#ninja.left(360 // (n * 2))  # Rotazione iniziale (commentala e vedi cosa succede)
i = 0                               # Inizializza il contatore

while i < n:                     # Fintanto che i è minore di n
    ninja.stamp()              # Lascia un'impronta del costume
    ninja.left(360 // n)       # Ruota così che in n volte compie un intero giro
    ninja.forward(passi)    # Avanza dei pixel specificato dalla variabile "passi"
    i = i + 1                      # Aggiorna il contatore (evita ciclo infinito)
