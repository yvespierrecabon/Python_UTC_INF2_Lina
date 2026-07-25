from random import choice


class Rectangle:
    def __init__(self, longueur:float, largeur:float):
        if longueur > 0 and largeur > 0:
            self.longueur = longueur
            self.largeur = largeur

    def get_longueur(self):
        return self.longueur
    def get_largeur(self):
        return self.largeur
    def set_longueur(self, longueur):
        self.longueur = longueur
    def set_largeur(self, largeur):
        self.largeur = largeur

    def perimetre(self):
        return 2 * self.longueur + self.largeur

    def aire(self):
        return 2 * self.longueur + self.largeur

    def est_carre(self)->bool:
        return self.longueur == self.largeur

    def le_plus_grand(self, other:"Rectangle")->"Rectangle":
        if self.aire()> other.aire():
            return self
        elif self.aire()<other.aire():
            return other
        else:
            return choice((self, other))

    def affiche(self):
        est_carre = "C'est un carré"
        if not self.est_carre():
            est_carre =  "Ce n'est pas un carré"
        print(f"Longueur : {self.longueur} - largeur : {self.largeur} "
              f"- perimetre : {self.perimetre()} - Aire : {self.aire()} - {est_carre}")




##########################################################

def main():
    rect_1 = Rectangle(10,10)
    rect_2 = Rectangle(10,8)
    rect_3 = Rectangle(6,10)

    rect_1.affiche()
    rect_2.affiche()
    rect_3.affiche()
    print("+ gd entre r1 et r2")
    rect_1.le_plus_grand(rect_2).affiche()
    print('r2 est carré : '+str(rect_2.est_carre()))


if __name__ == '__main__':
    main()


