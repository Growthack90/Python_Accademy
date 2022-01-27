def triangolo_rettangolo_ascii(n, car="*"):
    """Disegna un triangolo rettangolo col carattere specificato"""
    for riga in range(1, n  + 1):
        print(car * riga)
    
def triangolo_isoscele_ascii(n, car="*"):
    """Disegna un triangolo isoscele"""
    for riga in range(1, n  + 1):
        print(" " * (n - riga), end="") # Spazi bianchi: descrescono di 1 ad ogni riga
        print(car * (riga * 2 - 1))        # Asterischi: aumentano di 2 ad ogni riga

def quadrato_incorniciato_ascii(n, car1="*", car2="#"):
    """Disegna un quadrato di dimensione n con una cornice.
    Usa il carattere car1 per il bordo e car2 per la parte interna"""
    print(car1 * n)
    for riga in range(n - 2):
        print(car1, car2 * (n - 2), car1, sep="")
    print(car1 * n)
    
triangolo_isoscele_ascii(5)
