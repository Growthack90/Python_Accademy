"""Il programma "pensa" un numero tra 1 e 100 e chiede di indovinarlo"""
import random

MAX_N_TENTATIVI = 3
n_da_indovinare = random.randint(1, 100)
indovinato = False
tentativi = 1

# print("n_da_indovinare: "+ str(n_da_indovinare))

while not indovinato and tentativi <= MAX_N_TENTATIVI:
    prompt = "Tentativo "+ str(tentativi) +") Numero: "
    n = eval(input(prompt))
    
    if n_da_indovinare == n:
        print("\nComplimenti!")
        indovinato = True # Al prossimo controllo esce dal ciclo
    elif n > n_da_indovinare:
        print("Ho pensato un numero più piccolo\n")
    else:
        print("Ho pensato un numero più grande\n")
    
    tentativi += 1 # Prossimo tentativo

if not indovinato: # Posso anche controllare se tentativi > MAX_N_TENTATIVI
    print("Avevo pensato il numero", n_da_indovinare)
    print("Ritenta sarai più fortunato!")
