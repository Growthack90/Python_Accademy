"""Calcolo dell'interesse composto"""
# Dati iniziali
capitale_iniziale = 100
tasso = 0.03 # Corrisponde al 3%
n_anni = 10

# Elaborazione
capitale_finale = capitale_iniziale * (1 + tasso) ** n_anni

# Output
print("Dopo", n_anni, "anni il capitale è:", capitale_finale)                                      
print("Dopo", n_anni, "anni il capitale è:", round(capitale_finale, 2))                                      
