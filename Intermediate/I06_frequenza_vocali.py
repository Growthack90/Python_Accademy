import string

"""Legge un file di testo e valuta la frequenza vocali"""
def frequenza_vocali(s):
    """Data una stringa, ritorna la percentuale delle vocali
    dell’alfabeto italiano presenti in s
    in rapporto al numero totale delle lettere"""
    n_vocali = 0
    n_lettere = 0
    
    for car in s:
        if car.upper() in "AEIOU":
            n_vocali += 1
        if car.upper() in string.ascii_uppercase:
            n_lettere += 1
            
    return int(n_vocali / n_lettere * 100)

if __name__ == "__main__":
    s = "Nel mezzo del cammin di nostra vita"
    print("Testo:", s)
    print("Frequenza vocali: %i%%" % frequenza_vocali(s))
