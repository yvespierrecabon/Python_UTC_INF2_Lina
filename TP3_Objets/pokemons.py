from random import randint
from typing import Tuple


class Pokemon:
    def __init__(self, nom: str, pv: int, atk: int):
        self._nom = nom
        self._pv = pv
        self._atk = atk

    def get_nom(self) -> str:
        return self._nom

    def get_pv(self) -> int:
        return self._pv

    def set_pv(self, pv):
        self._pv = max(0,pv)

    def get_atk(self) -> int:
        return self._atk

    def __str__(self):
        return f"{self.get_nom()} - PV : {self.get_pv()} - ATK : {self.get_atk()}"

    def est_ko(self) -> bool:
        return self.get_pv() == 0

    def attaquer(self, other: "Pokemon"):

        print(f"{self.get_nom()} ({self.get_pv()} PV) Coeff mult : {self.calc_multiplicateur(other)} attaque {other.get_nom()} ({other.get_pv()} PV). ",end='')
        attaque = randint(0, self.get_atk())*self.calc_multiplicateur(other)
        print(f" dégat :{attaque} ",end='')
        other.set_pv(other.get_pv() - attaque)
        print(f"Après attaque {other.get_nom()} ({other.get_pv()} PV)")

    def combattre(self, other: "Pokemon") -> Tuple["Pokemon", int]:
        tour_attaque = 0
        while not self.est_ko() and not other.est_ko():
            self.attaquer(other)
            if not other.est_ko():
                other.attaquer(self)
            tour_attaque += 1
        if self.est_ko():
            return other, tour_attaque
        else:
            return self, tour_attaque

    def calc_multiplicateur(self, autre:"Pokemon")->float:
        return 1
##########################################################
class PokemonNormal(Pokemon):
    def __init__(self, nom: str, pv: int, atk: int):
        super().__init__(nom, pv, atk)

    def calc_multiplicateur(self, autre: "Pokemon") -> float:
        return 1


class PokemonFeu(Pokemon):
    def __init__(self, nom: str, pv: int, atk: int):
        super().__init__(nom, pv, atk)

    def calc_multiplicateur(self, autre:"Pokemon")->float:
        if isinstance(autre, PokemonPlante):
            return 2
        elif isinstance(autre, PokemonFeu) or isinstance(autre, PokemonEau):
            return 0.5
        else:
            return 1
        
            
class PokemonEau(Pokemon):
    def __init__(self, nom: str, pv: int, atk: int):
        super().__init__(nom, pv, atk)

    def calc_multiplicateur(self, autre:"Pokemon")->float:
        if isinstance(autre, PokemonFeu):
            return 2
        elif isinstance(autre, PokemonEau) or isinstance(autre, PokemonPlante):
            return 0.5
        else:
            return 1

class PokemonPlante(Pokemon):
    def __init__(self, nom: str, pv: int, atk: int):
        super().__init__(nom, pv, atk)

    def calc_multiplicateur(self, autre:"Pokemon")->float:
        if isinstance(autre, PokemonEau):
            return 2
        elif isinstance(autre, PokemonFeu) or isinstance(autre, PokemonPlante):
            return 0.5
        else:
            return 1

def main():
    pok1 = PokemonEau("pikachu", 8, 2)
    pok2 = PokemonFeu("pikacha", 5, 3)
    gagnant, nb_tour = pok1.combattre(pok2)
    print(f"Gagnant : {gagnant.get_nom()} en {nb_tour} tours")

if __name__ == "__main__":
    main()
