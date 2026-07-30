
class Balise:
    def __init__(self, nom: str, attributs: dict | None = None):
        self._nom: str = nom.lower()
        if attributs is not None:
            self._attributs: dict = attributs
        else:
            self._attributs: dict = {}

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def attributs(self) -> dict:
        return self._attributs

    @attributs.setter
    def attributs(self, nouveaux_attributs:dict):
        if not isinstance(nouveaux_attributs, dict):
            raise TypeError("attribut doit être un dictionnaire")
        self._attributs = nouveaux_attributs


class BaliseContenu(Balise):
    def __init__(self, nom: str,contenu: list, attributs: dict | None = None ):
        super().__init__(nom, attributs)
        self.contenu = contenu

    @property
    def contenu(self) -> list:
        return self._contenu
    @contenu.setter
    def contenu(self, contenu: list):
        if not isinstance(contenu, list):
            raise TypeError("Contenu must be a list")
        for val in contenu:
            if not (isinstance(val, str) or isinstance(val, Balise)):
                raise TypeError("Contenu invalide : uniquement texte ou Balise")
        self._contenu:list = contenu




def main():
    pass


if __name__ == '__main__':
    main()
