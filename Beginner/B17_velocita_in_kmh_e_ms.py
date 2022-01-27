"""Calcolo della velocità in km/h e m/s"""
# Dati iniziali
minuti = 21     # Tempo impiegato: 21' e 34''
secondi = 34
km = 4.1        # Distanza percorsa: 4,1 km

# Elaborazione
secondi_totali = minuti * 60 + secondi

# Velocità in m/s
metri = km * 1000
m_s = metri / secondi_totali
 
# Velocità in km/h, uso la seguente proporzione:
# km : km_h = secondi_totali : 3600
km_h = km * 3600 / secondi_totali

# Output
print("Velocità:", round(m_s, 2), "m/s")
print("Velocità:", round(km_h, 2), "km/h")
                                      

