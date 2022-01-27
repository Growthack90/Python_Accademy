def inversa(s):
    """Ritorna l'inversa di una stringa"""
    s_inversa = ""

    for carattere in s:
        s_inversa = carattere + s_inversa # Aggiunge il carattere in testa

    return  s_inversa

if __name__ == '__main__':
    print(inversa("AMOR"))
