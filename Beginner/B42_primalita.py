def is_primo(n):
    '''Ritorna True se n è primo, False in caso contrario'''
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False    # Ha trovato un divisore, non serve che prosegua

    return True    # Non ha trovato nessun divisore, quindi n è primo
