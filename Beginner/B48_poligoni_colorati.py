"""Disegna alcuni poligoni regolari colorati"""
import turtle

ninja = turtle.Turtle()
ninja.hideturtle()          # Rendi invisibile la tartaruga
ninja.pensize(10)

colori = "yellow", "red", "orange", "violet", "purple", "lightblue" # Elenco di colori
passi = 80
n_lati = 3    # Parti dal triangolo

for colore in colori:    # Per ogni "colore" nella lista "colori"
    ninja.color(colore) # Setta il colore della penna e di riempimento
    ninja.begin_fill()     # Inizia a disegnare una "forma piena"

    for lato in range(n_lati):      # Disegna un poligono regolare di n_lati
        ninja.forward(passi)        # Avanza dei pixel specificato dalla variabile "passi"
        ninja.left(360 / n_lati)      # Ruota così che in n volte compie un intero giro

    ninja.end_fill()            # Riempi di colore la forma disegnata
    ninja.forward(passi)   # Spostati per disegnare il nuovo poligono
    n_lati += 1                # Passa al poligono successivo come numero di lati
