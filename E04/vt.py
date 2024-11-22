import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import argparse

# Funzione argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description='Calcolo distanza percorsa da velocità.')
    parser.add_argument(
        '-f', '--file',    
        action='store',      
        default='https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/main/dati/integrazione_derivazione/vel_vs_time.csv',
        help='File di input'
    )
    parser.add_argument('-v', '--vel', action='store_true', help='Grafico Velocità vs Tempo')
    parser.add_argument('-d', '--dist', action='store_true', help='Grafico Distanza vs Tempo')
    return parser.parse_args()

def distanza():
    # Parse arguments
    args = parse_arguments()
    print(args)
    
    # Lettura file
    df0 = pd.read_csv(args.file)

    # Plot 1: Velocità vs. Tempo
    if args.vel:
        plt.figure(figsize=(12, 6))
        plt.plot(df0['t'], df0['v'], color='limegreen')
        plt.title("Velocità vs Tempo", fontsize=16)
        plt.xlabel('Tempo (t) [s]', fontsize=14)
        plt.ylabel('Velocità (v) [m/s]', fontsize=14)
        plt.grid(True)
        plt.show()

    # Plot 2: Distanza vs. Tempo
    if args.dist:
        distanza = []  # Array vuoto per la distanza
        for j in range(1, len(df0['v'])+1):
            # Integrazione usando Simpson
            dist = integrate.simpson(df0['v'][:j], dx=0.2)
            distanza.append(dist)

        plt.figure(figsize=(12, 6))
        plt.plot(df0['t'], distanza, color='blue')
        plt.title("Distanza vs Tempo", fontsize=16)
        plt.xlabel('Tempo (t) [s]', fontsize=14)
        plt.ylabel('Distanza (x) [m]', fontsize=14)
        plt.grid(True)
        plt.show()

# Esegui solo se il file è il main script
if __name__ == "__main__":
    distanza()
