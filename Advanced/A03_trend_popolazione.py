from turtle import *
from time import sleep

def trend(anno, pop_a, pop_b, tasso_a, tasso_b):
    """Calcola l'andamento (trend) delle popolazioni di A e di B
    e ritorna l'anno di parità della popolazione,
    supponendo che pop_a > pop_b e tasso_a < tasso_b"""
    if pop_a < pop_b or tasso_a > tasso_b:
        raise Exception("Pareggio impossibile!")

    while pop_a > pop_b:
        scrivi_popolazione(anno, pop_a, pop_b)
        pop_a += int(pop_a * tasso_a)
        pop_b += int(pop_b * tasso_b)
        anno += 1

    scrivi_popolazione(anno, pop_a, pop_b)
    return anno

def scrivi_popolazione(anno, pop_a, pop_b):
    """Stampa grafica e testuale dei dati: anno, popolazione di A, popolazione di B
    e della loro differenza percentuale
    """
    print(anno, pop_a, pop_b)
    tracer(0) # Velocità di disegno massima
    font = ("Arial", 20) # Font della famiglia Arial e dimensione 20 px
    penup()
    clear() # Pulisce il canvas
    diff_perc = str(int((pop_a - pop_b) / pop_a * 100))
    scrivi(anno, -100, 0)
    scrivi("Pop. A: "+ str(pop_a), 0, 30)
    scrivi("Pop. B: "+ str(pop_b), 0, -30)
    scrivi(diff_perc +"%", 200, 0)
    update() # Aggiorna (ridisegna) il canvas
    sleep(1) # Attendi 3 decimi di secondo

def scrivi(s, x, y):
    """Scrive una stringa in una posizione specifica canvas"""
    tracer(0)
    penup()
    goto(x, y)
    write(s, font=("Arial", 20)) # Usa un font di tipo Arial con dimensione 20

if __name__ == "__main__":
    anno_iniziale = 2017
    pop_a, pop_b = 100, 30 # Popolazioni iniziali di A e B
    tasso_a = 0.01 # Tasso di crescita annuale:  1%
    tasso_b = 0.30 # Tasso di crescita annuale: 30%
    anno = trend(anno_iniziale, pop_a, pop_b, tasso_a, tasso_b)
    print("L'anno del sorpasso è il {}".format(anno))
