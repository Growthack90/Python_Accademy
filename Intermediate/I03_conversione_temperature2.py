"""Il programma converte un valore di temperatura tra gradi Fahrenheit e gradi
Celsius (o centigradi), secondo la seguente formula di conversione:
T(°C) = (T(°F) – 32) / 1.8"""
import tkinter as tk

def conversione():
    gradi_celsius = round((fahrenheit.get() - 32) / 1.8, 2)
    celsius.set(str(gradi_celsius) +" °C")

if __name__ == "__main__":
    root = tk.Tk()    
    root.geometry("300x90") # Ridimensiona la finestra
    root.title("Conversione temperature")

    # Variabili da associare ai controlli
    fahrenheit = tk.DoubleVar()
    celsius = tk.DoubleVar()

    # Controlli
    label_fahrenheit = tk.Label(root, text="° Fahrenheit").pack()
    box_fahrenheit = tk.Entry(root, textvariable=fahrenheit).pack()
    label_celsius = tk.Label(root, textvariable=celsius).pack()
    button_esegui = tk.Button(root, text="Converti", command=conversione).pack()
    
    root.mainloop() # Loop di Tkinter: gestisce gli eventi fino alla chiusura della finestra
