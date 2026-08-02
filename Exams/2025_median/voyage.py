class Voyage:
    def __init__(self, destination:str, cout:float, duree:int):
        self.destination = destination
        self.cout = cout
        self.duree = duree

    @property
    def destination(self):
        return self._destination

    @property
    def cout(self):
        return self._cout

    @property
    def duree(self):
        return self._duree

    @destination.setter
    def destination(self, destination:str):
        self._destination = destination[:20]

    @cout.setter
    def cout(self, cout:float):
        self._cout = cout# This is a sample Python script.

    @duree.setter
    def duree(self, duree:float):
        self._duree = duree

    def __str__(self):
        return f"Destination : {self.destination}, durée {self.duree} jours, prix {self.cout:.02f} Euros"

class VoyageOrganise(Voyage):
    def __init__(self, destination:str, cout:float, duree:int):
        super().__init__(destination, cout, duree)
        self._nb_voyageurs = 0
        self._activites = {}

    def ajouter_voyageur(self, n:int):
        self._nb_voyageurs += n

    def ajouter_activite(self, activite:str, cout:float):
        self._activites[activite] = cout


    def calcul_cout(self):
        return self.cout + sum(self._activites.values())

    def __str__(self):
        txt = super().__str__()
        txt += f"\nNombre de voyageurs : {self._nb_voyageurs}\n"
        if self._activites:
            txt += "Activites :\n"
            for k,v in self._activites.items():
                txt += f"{k} : {v} Euros\n"
        cout_total = self.calcul_cout()
        txt += f"Prix total : {cout_total:.02f} Euros\n"
        return txt

    def __add__(self, other):
        self.destination += ", "+other.destination
        self.cout += other.cout
        self.duree += (1 + other.duree)
        self._nb_voyageurs += other._nb_voyageurs
        self._activites.update(other._activites)
        return self




def main():
    """voyage_org_1 = VoyageOrganise("Rome", 649, 4)
    voyage_org_1.ajouter_voyageur(40)
    voyage_org_1.ajouter_activite('visite du vatican',50)
    voyage_org_1.ajouter_activite('tour en scooter',100)
    print(voyage_org_1)"""

    voyage_org_1 = VoyageOrganise("Rome", 649, 4)
    voyage_org_1.ajouter_voyageur(20)
    voyage_org_1.ajouter_activite('visite du vatican',60)
    voyage_org_1.ajouter_activite('tour en scooter',100)
    print(voyage_org_1)

    voyage_org_2 = VoyageOrganise("Naples", 800, 6)
    voyage_org_2.ajouter_voyageur(25)
    voyage_org_2.ajouter_activite('excursion au Vésuve',127)
    print(voyage_org_2)

    try:
        voyage_3 = voyage_org_1 + voyage_org_2
    except TypeError():
        print()
        

    print(voyage_3)
if __name__ == '__main__':
    main()


