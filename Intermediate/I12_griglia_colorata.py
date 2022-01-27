"""Disegna una griglia colorata"""
import turtle

screen = turtle.Screen()    # Crea un riferimento alla finestra di disegno
screen.title("Griglia colorata")

ninja = turtle.Turtle()
ninja.speed(0)
ninja.pensize(10)
ninja.hideturtle()

passi = 50
n = 3

colori = "green", "red", "blue", "orange", "purple", "lightblue" # Elenco di colori

for i in range(n):
    ninja.penup()
    ninja.goto(-200, 200 - i*(passi + 12))    # Va avanti di "passi"
    ninja.pendown()

    for colore in colori:    # Per ogni "colore" nella lista "colori"
        ninja.color(colore)
        
        for j in range(4):
            ninja.forward(passi)    # Va avanti di "passi"
            ninja.left(90)          # Ruota di 45° gradi (45° x 8 = 360°)

        ninja.penup()
        ninja.forward(passi + 12)    # Va avanti di "passi"
        ninja.pendown()
    
