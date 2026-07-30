class Balise:
    def __init__(self, nom: str, attributs: dict | None = None):
        self._nom: str = nom.lower()
        if attributs:
            self._attributs: dict = attributs

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def attributs(self) -> dict:
        return self._attributs

    @attributs.setter
    def attributs(self, key, str, val: str):
        if key in self.attributs:
            self._attributs[key] = val


class BaliseContenu(Balise):
    def __init__(self, nom: str, contenu: str, **kwargs):
        Balise.__init__(self, nom, **kwargs)
        self.contenu = contenu.lower()


def main():
    pass


if __name__ == '__main__':
    main()
