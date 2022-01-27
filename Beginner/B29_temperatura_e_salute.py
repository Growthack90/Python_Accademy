"""Dà un responso sullo stato di salute in base alla temperatura inserita"""
temperatura = float(input("Temperatura: "))

if temperatura > 37:
    print("Hai la febbre")
    print("Riposati")
elif temperatura < 36:
    print("Sei un po' giù")
else:
    # Se si arriva qui vuol dire che la temperatura
    # è compresa tra 36 e 37
    print("Stai bene!")

print("Fine")
