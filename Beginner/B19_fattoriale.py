def fattoriale(n):
    """Ritorna il fattoriale di un numero.
    >>> fattoriale(5)
    120
    >>> fattoriale(6)
    20
    """
    risultato = 1

    for i in range(1, n + 1):
        risultato = risultato * i

    return risultato

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
