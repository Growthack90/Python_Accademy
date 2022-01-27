"""Calcolo dell'interesse composto con stampa anno per anno"""
def interesse_composto(n_anni):
    global capitale # Dichiara un riferimento alla variabile globale capitale
    
    for i in range(n_anni):
        anno = anno_iniziale + i

        # CODICE ERRATO
        #capitale = capitale*tasso # Aggiungi al capitale gli interessi annuali

        # CODICE CORRETTO
        capitale += capitale*tasso # Aggiungi al capitale gli interessi annuali

        print_capitale(anno, capitale)

    return capitale

def print_capitale(anno, capitale):
    print("{}\t{}".format(anno, round(capitale, 2)))
    
if __name__ == "__main__":
    capitale = 100
    tasso = 0.03 # Corrisponde al 3%
    n_anni = 5
    anno_iniziale = 2017
    interesse_composto(n_anni)
    print("Dopo", n_anni, "anni il capitale è:", round(capitale, 2))                                      
