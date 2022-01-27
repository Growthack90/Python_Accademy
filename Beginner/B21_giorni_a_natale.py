"""Calcola quanti giorni mancano a Natale"""
from datetime import date    # Importa dal modulo "datetime" il tipo "date"

oggi = date.today()
natale = date(2022, 12, 25)   # Gli argomenti sono nella forma: "aaaa, mm, gg"

print("Oggi:", oggi)
print("Giorni a Natale:", natale - oggi) # Sottrazione tra due date
