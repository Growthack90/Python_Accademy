"""Verifica se un numero è pari"""
def is_pari(n):
    """Ritorna True se n è pari, False in caso contrario"""
    return n % 2 == 0 # Ritorna True se e solo se il resto di n diviso 2 è 0

if __name__ == '__main__':
    # Blocco eseguito solo quando il programma viene eseguito direttamente.
    # Non viene eseguito se il modulo è importato da un altro programma
    n = eval(input("Numero: "))

    if is_pari(n):
        print(n, "è pari")
    else:
        print(n, "è dispari")    
