from datetime import datetime
from random import random as rd
import tkinter as tk

def date():
    return datetime.now().strftime("%d/%m/%Y")

def heure():
    return datetime.now().strftime("%H:%M:%S")

class JournalAlerte:
    def __init__(self, chemin_fichier:str):
        self._chemin_fichier = chemin_fichier
        with open(chemin_fichier, "w",encoding="utf-8") as f:
            f.write(f"---JOURNAL DES CRUES DU {date()}---\n")

    def ecrire_alerte(self, message:str):
        with open(self._chemin_fichier, "a",encoding="utf-8") as f:
            f.write(f"{message}\n")

class Capteur:
    def __init__(self, ville, journal:JournalAlerte):
        if type(ville) != str or not isinstance(journal, JournalAlerte):
            raise TypeError("Erreur dans le type des attributs du capteur")
        self._ville = ville
        self._journal = journal

    def mesure(self) ->float:
        return 1 + rd()*10

    def effectuer_releve(self):
        releve = self.mesure()
        message = f"R.A.S. {self._ville} ({releve:.2f} m)"
        if releve > 8:
            message=f"ALERTE [{heure()}] {self._ville} : niveau {releve:.2f} m"
            self._journal.ecrire_alerte(message)
        return message


class VigicruesApp(tk.Tk):
    def __init__(self, liste_capteurs:list):
        super().__init__()
        self.title("Vigicrues")
        self._capteurs = liste_capteurs
        self._releve = tk.StringVar()
        self.num_releve = tk.IntVar()
        tk.Label(self, text="Bienvenue\nSystème de monitoring").pack(pady=10)
        tk.Button(self, text="Relever les capteurs", command=self.declencher_mesures).pack(pady=5)
        tk.Label(self, textvariable=self._releve).pack(pady=10)

    def declencher_mesures(self) -> None:
        self.num_releve.set(self.num_releve.get()+1)
        self._releve.set(f"---Cycle de relevés n° {self.num_releve.get()}---\n\n")
        for capteur in self._capteurs:
            texte = self._releve.get()
            self._releve.set(texte + f"{capteur.effectuer_releve()}\n\n")
            

ja = JournalAlerte("journal.txt")
# ja.ecrire_alerte("hauteur d'eau à 18H00 : 2.15m")
capteur_1 = Capteur("Paris", ja)
capteur_2 = Capteur("Rouen", ja)
capteur_3 = Capteur("Melun", ja)
liste_capteurs = [capteur_1, capteur_2, capteur_3]
app = VigicruesApp(liste_capteurs)
app.mainloop()
