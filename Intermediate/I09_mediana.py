def mediana(valori):
    """Ritorna la mediana di una lista di valori"""
    v = valori[:] # Fa' una copia di valori
    v.sort() # Ordina in modo crescente i valori nella lista v
    n = len(v)
    
    if n % 2 != 0:
        m = v[n // 2] # n dispari
    else:
        m = (v[n // 2 - 1] + v[n // 2]) / 2 # n pari        

    return m

if __name__ == "__main__":
    altezze = [1.17, 1.24, 1.26, 1.27, 1.30, 1.30, 1.32]
    print(mediana(altezze))
    distanze = [121, 504, 167, 99]
    print(mediana(distanze))
