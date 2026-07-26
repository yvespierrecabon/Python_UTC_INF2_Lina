from typing import List, Dict


class ObjetCeleste:
    index:Dict[str,"ObjetCeleste"]={}

    def __init__(self, designation:str):
        self.liste_designation:List[str] = []
        self.ajouter_designation(designation)

    def ajouter_designation(self, designation:str):
        if designation in self.liste_designation:
            raise Exception(f"Designation {designation} already exists")
        self.liste_designation.append(designation)
        ObjetCeleste.index[designation] = self

    def get_designation(self):
        return self.liste_designation

    def __str__(self):
        return str(self.get_designation())

    @classmethod
    def get_objet_celeste(cls, designation:str):
        if designation in ObjetCeleste.index:
            return ObjetCeleste.index[designation]
        else:
            return None


class Etoile(ObjetCeleste):
    def __init__(self, designation:str, magnitude:float):
        super().__init__(designation)
        self.magnitude = magnitude

    def get_magnitude(self):
        return self.magnitude

    def set_magnitude(self, magnitude:float):
        if isinstance(magnitude, float):
            self.magnitude = magnitude


class Constellation(ObjetCeleste):
    def __init__(self, designation:str, etoile_1:Etoile, etoile_2:Etoile):
        super().__init__(designation)
        self.liste_etoile = []
        self.liste_etoile.append(etoile_1)
        self.liste_etoile.append(etoile_2)
        super().ajouter_designation(etoile_1.get_designation()[0])
        super().ajouter_designation(etoile_2.get_designation()[0])


    def ajouter_etoile(self, etoile:Etoile):
        if etoile in self.liste_etoile:
            self.liste_etoile.append(etoile)







def main():

    etoile1 = Etoile("Aldébaran", magnitude = 12.)
    etoile1.ajouter_designation("Alpha-Tau")
    etoile1.ajouter_designation("HR 1457")
    etoile2 = Etoile("Mars", magnitude = 18.)
    etoile3 = Etoile("Jupiter", magnitude = 19.)
    etoile4 = Etoile("Venus", magnitude = 24.)
    # etoile1.print()
    grande_ours = Constellation("Grande ours",etoile4,etoile3)
    #
    grande_ours.ajouter_etoile(etoile1)
    #
    # grande_ours.print()
    #
    print(ObjetCeleste.get_objet_celeste("Alpha-Tau"))
    print(ObjetCeleste.get_objet_celeste("Grande ours"))


if __name__ == "__main__":
    main()