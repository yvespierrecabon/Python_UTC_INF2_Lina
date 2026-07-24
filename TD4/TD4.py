
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

    @property
    def mort(self)->Date:
        if self._mort is None:
            raise ValueError("cette personne est encore vivante")
        else:
            return self._mort

    @mort.setter
    def mort(self, data_deces : Date)->None:
        if self.mort is not None:
            raise ValueError("Cette personne est déjà décédée")
        elif data_deces < self._naissance:
            raise ValueError("La mort ne peut précéder la naissance ...")
        else:
            self._mort = data_deces




##############################################################
# Classe Lien
##############################################################
class Lien :
    def __init__(self, i1:object, i2:object) :
        if not isinstance(i1, Individu) or not isinstance(i2, Individu):
            raise TypeError("type ’dindividu invalide ")
        self._lien= (i1, i2) # packing de i1 et i2 dans un tuple

        def __str__(self) -> str :
            return f"{self._lien[0]} et {self._lien[1]}"



##############################################################
# Classe Mariage
##############################################################
class Mariage(Lien):
    def __init__(self, i1:Individu, i2:Individu, date_mariage:Date) :
        super().__init__(i1, i2)
        self._date_mariage = date_mariage
        self._date_divorce = None

    def ajouter_divorce(self, date_divorce:Date) :
        if date_divorce < self._date_mariage:
            raise ValueError("La date du divorce ne peut précéder celle du mariage ...")
        self._date_divorce = date_divorce


    def __str__(self) -> str :
       texte = f"Mariage entre {super().__str__()}"
       if self._date_divorce is not None:
           texte += f" . Divorce le {self._date_divorce}"
       return texte





###############################################################


def main():
    """date = Date(1, 1, 2026)
    while date.a == 2026:  # Tant qu'on est en 2026
        print(date, end=" ")
        date = date.lendemain()
        if date.j == 1:
            print()  # Saut de ligne pour chaque nouveau mois"""

    Laura_Dupond = Individu("Dupond", "laura", Date(5,2,1986))
    Paul_berger = Individu("Berger", 'paul', Date(1,7,1985))

    mariage = Mariage(Laura_Dupond, Paul_berger, Date(25,2,2012))
    Claire_dupond_Berger = Individu('Dupond-Berger','Claire',Date(1,7,1985))
    mariage.ajouter_divorce(Date(26,8,2018))
    print(Laura_Dupond)
    print(Paul_berger)
    print(Claire_dupond_Berger)
    print(mariage)
    mariage.ajouter_divorce(Date(26,8,2018))
    print(mariage)
    Paul_berger.mort = Date(10,9,2024)
    print(Paul_berger)



if __name__ == "__main__":
    main()