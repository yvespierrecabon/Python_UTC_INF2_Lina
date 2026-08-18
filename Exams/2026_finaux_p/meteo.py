import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk

matplotlib.use('TkAgg')


villes = np.array(["Paris","Lyon","Nice","Strasbourg","Toulouse","Brest"])

temperatures = np.array([
    [33,37,37,36,37,39,41,41,39],
    [34,36,36,37,38,39,38,40,39],
    [27,26,28,28,30,32,33,32,32],
    [32,36,37,36,37,37,38,38,38],
    [37,36,34,35,38,39,40,37,38],
    [21,25,22,24,28,34,36,36,25]
])


def plus_grand_ecart(temp, villes):
    return villes[np.argmax([t.max() -t.min() for t in temp])]

def jour_plus_chaud(temp):
    jpc = np.array([temp[:,i].mean() for i in range(len(temp))])
    return jpc.max(), np.argmax(jpc)

def affiche_courbes(temp, villes):
    j = [i for i in range(len(temp[0,:]))]
    for k,t in enumerate(temp):
        plt.plot(j,t,'-o',label=villes[k])

    plt.title("Evolution des températures")
    plt.legend()
    plt.grid(True)
    plt.xlabel("jour")
    plt.ylabel("température (°C)")
    plt.show()
def simulation(temperatures, villes_, villes_travaux):
    indices_villes_travaux = np.where(np.isin(villes_,villes_travaux))[0]
    print(indices_villes_travaux)
    for v_ind in indices_villes_travaux:
        temperatures[v_ind] = temperatures[v_ind] *0.9
    affiche_courbes(temperatures, villes_)

class Fenetre(tk.Tk):
    def __init__(self, temperatures, villes):
        tk.Tk.__init__(self)
        self.title('évolution des températures')
        geometrie = f"{600}x{400}"
        self.geometry(geometrie)
        self._temperatures = temperatures
        self._villes = villes
        self._villes_travaux=["Paris","Toulouse","Lyon"]
        self.message=tk.StringVar()

        tk.Label(self, textvariable=self.message).grid(column=1, row=2, columnspan=2)
        tk.Button(self, text='jour plus chaud', command=self.affiche_plus_chaud).grid(column=1, row=3)

    def affiche_plus_chaud(self):
        temp, jour = jour_plus_chaud(self._temperatures)
        self.message.set(f"Jour le plus chaud : jour {jour} avec {temp:.1f} °C")


def main():
    print(plus_grand_ecart(temperatures, villes))
    print(jour_plus_chaud(temperatures))
    # affiche_courbes(temperatures, villes)
    simulation(temperatures, villes, np.array(["Toulouse","Paris"]))
    ma_fenetre = Fenetre(temperatures, villes)
    ma_fenetre.mainloop()


if __name__ == "__main__":
    main()
