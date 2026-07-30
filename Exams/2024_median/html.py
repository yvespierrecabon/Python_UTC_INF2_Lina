class Balise:
    def __init__(self, nom: str, attributs: dict | None = None):
        self._nom: str = nom.lower()
        self._attributs: dict | None = {}
        if attributs:
            self._attributs: dict = attributs

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def attributs(self) -> dict:
        return self._attributs

    @attributs.setter
    def attributs(self, nouveaux_attributs:dict | None):
        self._attributs = nouveaux_attributs


class BaliseContenu(Balise):
    def __init__(self, nom: str,contenu: list, attributs: dict | None = None ):
        Balise.__init__(self, nom, attributs)
        self._contenu:list = contenu

    @property
    def contenu(self) -> str:
        return self._contenu
    @contenu.setter
    def contenu(self, contenu: list):
        if not isinstance(contenu, list):
            raise TypeError("Contenu must be a list")
        self._contenu = contenu




def main():
    pass


if __name__ == '__main__':
    main()
