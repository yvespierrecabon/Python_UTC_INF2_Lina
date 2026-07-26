from datetime import datetime
from typing import List


class Covoit:
    def __init__(
        self,
        login: str,
        ville_source: str,
        ville_destination: str,
        date_depart: datetime,
        nb_place: int,
    ):
        self._login = login
        self._ville_source = ville_source
        self._ville_destination = ville_destination
        self._date_depart = date_depart
        self._nb_place = nb_place
        self._passagers = []

    def get_login(self):
        return self._login

    def get_ville_source(self):
        return self._ville_source

    def get_ville_destination(self):
        return self._ville_destination

    def get_date_depart(self) -> datetime:
        return self._date_depart

    def ajouter_passager(self, login: str):
        if login == self._login:
            print("Le passager ne peut pas être conducteur")
            return
        if login in self._passagers:
            print("Le passager est déjà passager")
            return
        if len(self._passagers) >= self._nb_place:
            print("Covoit plein")
            return
        else:
            self._passagers.append(login)


    def supprimer_passager(self, login: str):
        if login in self._passagers:
            self._passagers.remove(login)
        else:
            print("Impossible de supprimer", login)

    def __eq__(self, other):
        return (
            self._login == other.get_login()
            and self._ville_source == other.get_ville_source()
            and self._ville_destination == other.get_ville_destination()
            and self._date_depart == other.get_date_depart()
        )

    def __str__(self):
        return f"Conducteur : {self._login} - Départ : {self._ville_source} - Destination : {self._ville_destination}"


def calcul_decalage(date_1: datetime, date_2: datetime) -> int:
    return (date_2 - date_1).seconds // 60


def ajouter_un_covoiturage(covoit: "Covoit", covoits: List["Covoit"]):
    if covoit not in covoits:
        covoits.append(covoit)


def rechercher_covoiturage(
    covoits: List["Covoit"],
    date_depart: datetime,
    ville_source: str,
    ville_destination: str,
):
    covoits_ok = []
    for covoit in covoits:
        if (
            abs(calcul_decalage(covoit.get_date_depart(), date_depart)) < 60
            and covoit.get_ville_source() == ville_source
            and covoit.get_ville_destination() == ville_destination
        ):
            covoits_ok.append(covoit)
    return covoits_ok


def main():
    covoits: List[Covoit] = []
    c1 = Covoit("Loïc", "Compiegne", "Rennes", datetime(2022, 4, 18, 9, 40), 4)
    c1.ajouter_passager("Manon")
    c1.ajouter_passager("Jean")
    c1.ajouter_passager("Maxime")
    c1.ajouter_passager("Maxime")
    c1.ajouter_passager("non existant")  # affiche Erreur
    c1.ajouter_passager("Lola")
    c2 = Covoit("Loïc", "Rennes", "Compiègne", datetime(2022, 4, 18, 10, 40), 4)
    c3 = Covoit("Thomas", "Rennes", "Compiègne", datetime(2022, 4, 18, 9, 40), 4)
    print(c3 == c2)  # True
    ajouter_un_covoiturage(c1, covoits)
    ajouter_un_covoiturage(c2, covoits)
    ajouter_un_covoiturage(c3, covoits)
    for covoit in rechercher_covoiturage(covoits, datetime(2022, 4, 18, 9, 40), 'Rennes', 'Compiègne'):
        print(covoit)


if __name__ == "__main__":
    main()
