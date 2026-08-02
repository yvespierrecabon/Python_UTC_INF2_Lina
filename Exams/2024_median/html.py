import os.path


class Balise:
    _compteur = 0
    def __init__(self, nom: str, attributs: dict | None = None):
        Balise._compteur += 1
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

    def __str__(self):
        attrs = " " + " ".join(f'{k}="{v}"' for k, v in self.attributs.items()) if self.attributs else ""
        return f"<{self.nom}{attrs}>"

class BaliseContenu(Balise):
    def __init__(self, nom: str,contenu: list, attributs: dict | None = None ):
        super().__init__(nom, attributs)
        self._contenu: list
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

    def __str__(self):
        attrs = " " + " ".join(f'{k}="{v}"' for k, v in self.attributs.items()) if self.attributs else ""
        contenu_str = "\n".join(str(c) for c in self.contenu)
        return f"<{self.nom}{attrs}>\n{contenu_str}\n</{self.nom}>"

class Html(BaliseContenu):
    def __init__(self, contenu: list, attributs: dict | None = None):
        super().__init__('html', contenu, attributs)


class Titre(BaliseContenu):
    def __init__(self, niveau:str, contenu: list, attributs: dict | None = None):
        super().__init__(niveau, contenu, attributs)
        # self.niveau = niveau


class Paragraphe(BaliseContenu):
    def __init__(self, contenu: list, attributs: dict | None = None):
        super().__init__('p', contenu, attributs)


class Gras(BaliseContenu):
    def __init__(self, contenu: list, attributs: dict | None = None):
        super().__init__('b', contenu, attributs)



class Image(Balise):
    def __init__(self, attributs: dict | None = None):
        if attributs is None:
            attributs = {}
        if 'src' not in attributs or not os.path.exists(attributs['src']):
            raise ValueError("pas d'attribut src ou chemin incorrect")
        super().__init__('img', attributs)



def main():

    titre_1= Titre("h2",["Mon titre"])
    texte_gras_1 = Gras(["bout de paragraphe écrit en gras"])
    texte_gras_2 = Gras(["bout de paragraphe écrit en gras"])
    paragraphe_1= Paragraphe(["bout de paragraphe normal",texte_gras_1], {"style":"color:blue"})
    img_1= Image({'src':'20230416_001.jpg','width':'200','height':'120'})
    html_1= Html([titre_1,paragraphe_1,img_1,texte_gras_2])
    print(html_1)
    print(f"\nCe texte comporte {Balise._compteur} balises")


if __name__ == '__main__':
    main()
