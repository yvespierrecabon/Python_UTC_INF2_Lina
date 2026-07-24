from lief import exception


class Date:
    JOURS_MAX = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, j: int, m: int, a: int):
        self.set_annee(a)
        self.set_mois(m)
        self.set_jour(j)

    def get_jour(self) -> int:
        return self.j

    def set_jour(self, j: int) -> None:
        if 1 <= j <= self.JOURS_MAX.get(self.m, 0):
            self.j = j
        else:
            raise ValueError(f"Le jour {j} est invalide pour le mois {self.m}.")



    def get_mois(self) -> int:
        return self.m

    def set_mois(self, m: int) -> None:
        if 1 <= m <= 12:
            self.m = m
        else:
            raise ValueError(f"Le mois {m} doit être compris entre 1 et 12.")

    def get_annee(self) -> int:
        return self.a

    def set_annee(self, a: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise ValueError(f"L'année {a} doit être strictement positive.")

    def lendemain(self)->"Date":

        new_j = self.j + 1
        new_m = self.m
        new_a = self.a
        if new_j > Date.JOURS_MAX.get(new_m, 0):
            new_j = 1
            new_m += 1
            if new_m > 12:
                new_m = 1
                new_a += 1
        return Date(new_j, new_m, new_a)

    def __str__(self):
        return f'{self.j:02d}/{self.m:02d}/{self.a}'

    def __lt__(self, other: "Date") -> bool:
        if self.a != other.a:
            return self.a < other.a
        if self.m != other.m:
            return self.m < other.m
        return self.j < other.j


##############################################################
# Classe Individu
##############################################################
class Individu:
    def __init__(self, nom:str, prenoms:str, naissance:Date):
        self._nom = nom
        self._prenoms = prenoms
        self._naissance = naissance
        self._mort = None

    def est_mort(self)->bool:
        return self._mort is not None

    def __str__(self):
        return self._prenoms+" "+self._nom

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def prenoms(self) -> str:
        return self._prenoms

    @property
    def naissance(self) -> Date:
        return self._naissance

    @mort.setter
    def mort(self, data_deces : Date)->Date|None:
        if self.mort is not None or data_deces < self._naissance:
            raise Exception("Cette personne est déjà décédée")
        elif data_deces < self._naissance:
            raise Exception("La mort ne peut précéder la naissance ...")
        else:
            self._mort = data_deces




    





###############################################################


##############################################################
# Classe Mariage
##############################################################
"""class Mariage:
    def __init__(self):"""



###############################################################


def main():
    date = Date(1, 1, 2026)
    while date.a == 2026:  # Tant qu'on est en 2026
        print(date, end=" ")
        date = date.lendemain()
        if date.j == 1:
            print()  # Saut de ligne pour chaque nouveau mois




if __name__ == "__main__":
    main()