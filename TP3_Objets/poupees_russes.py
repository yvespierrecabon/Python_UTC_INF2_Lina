from sympy import false


class Poupee_russe:

    def __init__(self, nom:str, taille:int):
        self._nom = nom
        self._taille = taille
        self._est_ouverte = False
        self._dans = None
        self._contient = None

    @property
    def nom(self):
        return self._nom
    @property
    def taille(self):
        return self._taille
    @property
    def est_ouverte(self):
        return self._est_ouverte
    @property
    def dans(self):
        return self._dans
    @property
    def contient(self):
        return self._contient

    @est_ouverte.setter
    def est_ouverte(self, est_ouverte:bool)->None:
        self._est_ouverte = est_ouverte

    @dans.setter
    def dans(self, dans):
        self._dans = dans

    @contient.setter
    def contient(self, contient):
        self._contient = contient

    def ouvrir(self):
        if self.dans is None:
            self.est_ouverte = True

    def fermer(self):
        if self.dans is None:
            self.est_ouverte = False

    def placer_dans(self, p:'Poupee_russe')->bool:
        if self.dans is None and p.contient is None and self.est_ouverte is False and p.est_ouverte is True and p.taille > self.taille:
            self.dans = p
            p.contient = self
            return True
        else:
            return False


    def sortir_de(self):
        if self.dans is not None and self.dans.est_ouverte is True:
            self.dans.contient = None
            self.dans = None


    def __str__(self):
        texte = "Poupée russe : "+self.nom+"\n"

        poupee_courante = self.dans
        while poupee_courante is not None:
            texte += "contenue dans "+poupee_courante.nom+" "
            poupee_courante = poupee_courante.dans
        if self.dans is not None:
            texte += "\n"
        poupee_courante = self.contient
        while poupee_courante is not None:
            texte += "contient "+poupee_courante.nom+" "
            poupee_courante = poupee_courante.contient
        texte +="\n"
        return texte


##########################################################

def main():
    p1 = Poupee_russe(nom="p1", taille=10)
    p1.ouvrir()
    p2 = Poupee_russe(nom="p2", taille=9)
    p2.ouvrir()
    p3 = Poupee_russe(nom="p3", taille=8)
    p3.placer_dans(p2)
    p2.fermer()
    p2.placer_dans(p1)

    print(p1)
    print(p2)
    print(p3)

    p1.ouvrir()
    p2.sortir_de()
    print("Sortie de P2 de P1\n")
    print(p1)
    print(p2)
    print(p3)

if __name__ == '__main__':
    main()
