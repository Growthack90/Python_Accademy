"""Semplice calcolatrice"""
separatore = "-" * 60
operazione = ""

while True:
    operazione = input('Operazione (1=addizione, 2=sottrazione, 0=Fine): ')

    try:
        if operazione in ("1", "2"):
            op1 = eval(input("Primo operando: "))
            op2 = eval(input("Secondo operando: "))

        if operazione == "1":
            risultato = op1 + op2
        elif operazione == "2":
            risultato = op1 - op2
        elif operazione == "0":
            exit(0) # Termina il programma senza errori (0)
        else:
            risultato = "Operazione non prevista"
    except:        
        risultato = "Errore"

    print(separatore)
    print("Out:", risultato)
