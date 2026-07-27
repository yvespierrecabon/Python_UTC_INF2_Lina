from typing import List, Dict, Optional

class ObjetCeleste:
    index: Dict[str, "ObjetCeleste"] = {}

    def __init__(self, designation: str):
        self._liste_designation: List[str] = []
        self.ajouter_designation(designation)

    def ajouter_designation(self, designation: str)->None:
        if not isinstance(designation, str):
            raise TypeError("La désignation doit être de type str")
        if designation in self._liste_designation:
            raise ValueError(f"Designation {designation} already exists")
        self._liste_designation.append(designation)
        ObjetCeleste.index[designation] = self

    def get_designations(self):
        return self._liste_designation

    def __str__(self) -> str:
        return f"ObjetCeleste(désignations={self.get_designations()})"

    @classmethod
    def get_objet_celeste(cls, designation: str) -> Optional["ObjetCeleste"]:
        if designation in ObjetCeleste.index:
            return ObjetCeleste.index[designation]
        else:
            return None


class Etoile(ObjetCeleste):
    def __init__(self, designation: str, magnitude: float):
        super().__init__(designation)
        self._magnitude = magnitude

    def get_magnitude(self) -> float:
        return self._magnitude

    def set_magnitude(self, magnitude: float) -> None:
        if not isinstance(magnitude, (int, float)):
            raise TypeError("Magnitude doit être un nombre (int ou float)")
        self._magnitude = float(magnitude)

    def __str__(self) -> str:
        return f"Etoile(désignations={self.get_designations()}, magnitude={self.get_magnitude()})"


class Constellation(ObjetCeleste):
    def __init__(self, designation: str, etoile_1: Etoile, etoile_2: Etoile):
        super().__init__(designation)
        self._liste_etoile = []
        self._liste_etoile.append(etoile_1)
        self._liste_etoile.append(etoile_2)

    def ajouter_etoile(self, etoile: Etoile) -> None:
        if not isinstance(etoile, Etoile):
            raise TypeError("L'étoile doit être de type Etoile")
        if etoile in self._liste_etoile:
            raise ValueError("Étoile déjà présente dans la constellation")
        self._liste_etoile.append(etoile)

    def __str__(self) -> str:
        return f"Constellation(désignations={self.get_designations()}, étoiles={len(self._liste_etoile)})"


def main():
    etoile1 = Etoile("Aldébaran", magnitude=12.0)
    etoile1.ajouter_designation("Alpha-Tau")
    etoile1.ajouter_designation("HR 1457")
    etoile2 = Etoile("Mars", magnitude=18.0)
    etoile3 = Etoile("Jupiter", magnitude=19.0)
    etoile4 = Etoile("Venus", magnitude=24.0)
    # etoile1.print()
    grande_ours = Constellation("Grande ourse", etoile4, etoile3)
    #
    grande_ours.ajouter_etoile(etoile1)
    #
    # grande_ours.print()
    #
    print(ObjetCeleste.get_objet_celeste("Alpha-Tau"))
    print(ObjetCeleste.get_objet_celeste("Grande ourse"))


if __name__ == "__main__":
    main()
