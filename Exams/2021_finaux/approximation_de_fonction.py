import matplotlib
from matplotlib.lines import lineStyles

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

def f(x, c1, c2):
    return c1 * np.exp(-x) + c2 * x

def main():
    c1 = 5
    c2 = 2
    x = np.arange(0, 1, 0.01)
    yinit = f(x, c1, c2)
    perturbations = np.random.uniform(-1, 1, size=len(yinit))
    yi = yinit + 0.05*max(yinit)*perturbations

    A = np.column_stack((np.exp(-x), x))
    c1_res, c2_res = np.linalg.lstsq(A, yi, rcond=None)[0]
    y_res = f(x, c1_res, c2_res)

    plt.plot(x, yinit, 'r-', label='fonction initiale')
    plt.plot(x, yi, 'x', label='échantillons')
    plt.plot(x,y_res, 'g', linestyle = 'dashed' ,label='approximation')
    plt.xlabel('x')  # Label de l'axe x
    plt.ylabel('y')  # Label de l'axe y
    plt.title('Final 2021')  # Titre du graphique
    plt.grid(True)  # Grille pour une meilleure lisibilité
    plt.legend()  # Affiche la légende
    plt.show()  # Affiche le graphique

if __name__ == "__main__":
    main()