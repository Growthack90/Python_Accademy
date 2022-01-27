def fibonacci(n):
    """Ritorna l'n-simo valore della serie di Fibonacci"""
    a, b = 1, 1 # a = num. coppie al primo mese, b al secondo mese

    for i in range(1, n + 1):
        a, b = b, a + b  # Va in avanti con le coppie nei mesi successivi
        
    return a
