def cripta_farfallino(messaggio):
    """Dato un messaggio ne ritorna una versione criptata secondo l'alfabeto farfallino."""
    messaggio_criptato = ""    

    for car in messaggio:
        if car in "aeiou":
            messaggio_criptato += car +"f"+ car 
        elif car in "AEIOU":
            messaggio_criptato += car +"F"+ car 
        else:
            # Ricopia così com'è tutto ciò che non è una vocale
            messaggio_criptato += car             

    return messaggio_criptato

def decripta_farfallino(messaggio):
    """Dato un messaggio criptato ritorna il corrispondente messaggio originale"""
    messaggio_decriptato = messaggio    

    for codice in ("afa", "efe", "ifi", "ofo", "ufu", "AFA", "EFE", "IFI", "OFO", "UFU"):
        vocale = codice[0]
        messaggio_decriptato = messaggio_decriptato.replace(codice, vocale)            

    return messaggio_decriptato

frase = "Effetto farfalla e teoria del caos"
print(cripta_farfallino(frase))
print(decripta_farfallino(cripta_farfallino(frase)))

