"""Programma che analizza le frequenze delle lettere in testi in italiano e in inglese"""
import string

def occorrenze_vocali(testo, lettere):
    """Ritorna un dizionario con la frequenza delle lettere indicate"""
    occorrenze = {} # Dizionario con il numero di occorrenze delle lettere
    freq = {} # Dizionario con la frequenza delle lettere
    tot = 0  # Contatore di tutte le lettere
    
    for car in testo.upper():
        if car in lettere:
            if car not in occorrenze:
                occorrenze[car] = 0
            else:
                occorrenze[car] += 1
            tot += 1
            
    # Crea un dizionario con le frequenze dei singoli caratteri
    for car, valore in occorrenze.items():
        freq[car] = valore / tot # Aggiunge un elemento con la chiave e la frequenza
    
    return freq

def frequenze_in_testo(filename, lettere=string.ascii_uppercase):
    """Ritorna la frequenza delle vocali di un file di testo"""
    file = open(filename, "r")
    testo = file.read() # Carica tutto il contenuto del file nella variabile testo
    file.close() # Ciò che è stato aperto va chiuso
    return occorrenze_vocali(testo, lettere)

def str_frequenze(frequenze, lettere):
    """Ritorna una stringa con le frequenze delle lettere indicate"""
    s = ""
    for car in lettere:
        # Carattere e frequenza in percentuale in un campo di 5 caratteri in totale
        s += "{}:{:05.2f}%  ".format(car, frequenze[car] * 100)
    return s

if __name__ == '__main__':
    freq_it = frequenze_in_testo("pinocchio.txt")
    freq_en = frequenze_in_testo("oz.txt")
    print("Pinocchio (it):\t", str_frequenze(freq_it, lettere="AEIOUY"))
    print("Oz (en):\t", str_frequenze(freq_en, lettere="AEIOUY"))

    freq_it = frequenze_in_testo("i_promessi_sposi.txt")
    freq_en = frequenze_in_testo("doctor_jekyll.txt")
    print("I promessi sposi (it):\t", str_frequenze(freq_it, lettere="JKWXY"))
    print("Lo strano caso... (en):\t", str_frequenze(freq_en, lettere="JKWXY"))
