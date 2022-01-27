"""Mostra la differenza tra variabili locali e globali"""
def print_successivo(n):
    var = 3 # var e n sono visibili solo all'interno della funzione
    n += 1 # Modifica e stampa la variabile n locale
    print("n locale:", n)

if __name__ == '__main__':
    n = 10
    print("n globale prima:", n)
    print_successivo(n)
    print("n globale dopo:", n)