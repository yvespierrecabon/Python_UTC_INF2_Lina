import os.path


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


class Html(BaliseContenu):
    def __init__(self, contenu: list, attributs: dict | None = None):
        super().__init__('html', contenu, attributs)
        
    def __str__(self):
        attrs = ""
        if len(self.attributs) >0:
            attrs=" "
            for k,v in self.attributs.items():
                attrs += f"{k}='{v}' "
        texte = f"<html{attrs}>\n"
        for contenu_ in self.contenu:
            texte += f"{contenu_}\n"
        return texte + "</html>"
        


class Titre(BaliseContenu):
    def __init__(self, contenu: list, attributs: dict | None = None):
        super().__init__('h1', contenu, attributs)

    def __str__(self):
        attrs = ""
        if len(self.attributs) >0:
            attrs=" "
            for k,v in self.attributs.items():
                attrs += f"{k}='{v}' "
        texte = f"<h1{attrs}"
        for contenu_ in self.contenu:
            texte += f"{contenu_}\n"
        return texte + "</h1>"

class Paragraphe(BaliseContenu):
    def __init__(self, contenu: list, attributs: dict | None = None):
        super().__init__('p', contenu, attributs)

    def __str__(self):
        attrs = ""
        if len(self.attributs) >0:
            attrs=" "
            for k,v in self.attributs.items():
                attrs += f"{k}='{v}' "
            texte = f"<p{attrs}>\n"

            for contenu_ in self.contenu:
                texte += f"{contenu_}\n"
            return texte + "</p>"


class Gras(BaliseContenu):
    def __init__(self, contenu: list, attributs: dict | None = None):
        super().__init__('b', contenu, attributs)

    def __str__(self):
        attrs = ""
        if len(self.attributs) >0:
            attrs=" "
            for k,v in self.attributs.items():
                attrs += f"{k}='{v}' "
        texte = f"<b{attrs}>\n"
        for contenu_ in self.contenu:
            texte += f"{contenu_}\n"
        return texte + "</b>"


class Image(Balise):
    def __init__(self, attributs: dict | None = None):
        if 'src' in attributs.keys() and os.path.exists(attributs['src']):
            super().__init__('img', attributs)
            self._path:str = attributs['src']
        else:
            raise ValueError("pas d'attribut src ou chemin incorrect")




def main():

    titre_1= Titre(["Mon titre"])
    texte_gras_1 = Gras(["bout de paragraphe écrit en gras"])
    paragraphe_1= Paragraphe(["bout de paragraphe normal",texte_gras_1], {"style":"color:blue"})
    html_1= Html([titre_1,paragraphe_1, 'ceci est un texte en html', '1'],{'test':'test1'})
    print(html_1)


if __name__ == '__main__':
    main()
