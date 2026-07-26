from typing import List, Dict


class ObjetCeleste:
    index:Dict[str,"ObjetCeleste"]={}

    def __init__(self, designation:str):
        self._liste_designation:List[str] = []
        self.ajouter_designation(designation)

    def ajouter_designation(self, designation:str):
        if designation in self._liste_designation:
            raise ValueError(f"Designation {designation} already exists")
        self._liste_designation.append(designation)
        ObjetCeleste.index[designation] = self

    def get_designations(self):
        return self._liste_designation

    def __str__(self):
        return str(self.get_designations())

    @classmethod
    def get_objet_celeste(cls, designation:str):
        if designation in ObjetCeleste.index:
            return ObjetCeleste.index[designation]
        else:
            return None


class Etoile(ObjetCeleste):
    def __init__(self, designation:str, magnitude:float):
        super().__init__(designation)
        self._magnitude = magnitude

    def get_magnitude(self):
        return self._magnitude

    def set_magnitude(self, magnitude:float):
        if isinstance(magnitude, float):
            self._magnitude = magnitude


class Constellation(ObjetCeleste):
    def __init__(self, designation:str, etoile_1:Etoile, etoile_2:Etoile):
        super().__init__(designation)
        self._liste_etoile = []
        self._liste_etoile.append(etoile_1)
        self._liste_etoile.append(etoile_2)
        super().ajouter_designation(etoile_1.get_designations()[0])
        super().ajouter_designation(etoile_2.get_designations()[0])


    def ajouter_etoile(self, etoile:Etoile):
        if etoile not in self._liste_etoile:
            self._liste_etoile.append(etoile)







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