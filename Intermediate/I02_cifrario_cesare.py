"""Programma che implementa il cifrario di Cesare"""
import string

def codifica(msg, chiave=3):
    """Ritorna un messaggio codificato con uno spostamento di default di 3 posizioni"""
    msg_codificato = ""
    for car in msg:
        if car in string.ascii_uppercase:
            index = ord(car) + chiave # Calcola l'indice del carattere  cifrato
            if index > ord('Z'):             # Se l'indice va oltre 'Z'
                index = index - 26         # Riparti in modo circolare da 'A'
            msg_codificato += chr(index)
        else:
            msg_codificato += car # Copia i caratteri che non sono lettere
    return msg_codificato

def decodifica(msg, chiave=3):
    """Ritorna un messaggio decodificato con uno spostamento di default di 3 posizioni"""
    msg_decodificato = ""
    for car in msg:
        if car in string.ascii_uppercase:
            index = ord(car) - chiave # Calcola l'indice del carattere decifrato
            if index < ord('A'):            # Se l'indice va "sotto" 'A'
                index = index + 26       # Riparti in modo circolare da 'Z'
            msg_decodificato += chr(index)
        else:
            msg_decodificato += car # Copia i caratteri che non sono lettere
    return msg_decodificato

def codifica2(msg, chiave=3):
    """Ritorna un messaggio decodificato con uno spostamento di default di 3 posizioni"""
    msg_codificato = ""
    for car in msg:
        if car in string.ascii_uppercase:
            index = (ord(car) + chiave - ord('A')) % 26
            msg_codificato += chr(ord('A') + index)
        else:
            msg_codificato += car # Copia i caratteri che non sono lettere
    return msg_codificato


messaggio = "ARRESTATE ASTERIX, OBELIX E IL VECCHIO DRUIDO!"
print(codifica(messaggio))
print(decodifica(codifica(messaggio)))
print(decodifica(codifica2(messaggio)))
