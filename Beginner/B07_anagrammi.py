import string

def is_anagramma(s1, s2):
    """Ritorna True se le due stringhe sono anagrammi, False in caso contrario"""
    occorrenze_s1 = occorrenze_lettere(s1)
    occorrenze_s2 = occorrenze_lettere(s2)

    for car in string.ascii_uppercase:
        if occorrenze_s1[car] != occorrenze_s2[car]:
            return False # Ho trovato un numero di occorrenze diverso

    return True

def occorrenze_lettere(s):    
    """Ritorna un dizionario con le lettere dell'alfabeto maiuscole e le loro
    occorrenze nella stringa s, senza distinzione tra maiuscolo e minuscolo"""
    occorrenze = {}

    for car in string.ascii_uppercase: # Pone i contatori a 0 per tutte le lettere
        occorrenze[car] = 0
        
    for car in s.upper():
        if car in string.ascii_uppercase:
            occorrenze[car] += 1 # Quando trova una lettera aggiorna il suo contatore

    return occorrenze

print(is_anagramma("nave", "vena"))
print(is_anagramma("bibliotecario", "beato coi libri"))
print(is_anagramma("visione d’arte", "rosa dei venti"))
print(occorrenze_lettere("Nel mezzo del cammin di nostra vita mi ritrovai..."))
