class Balise:
    def __init__(self, nom:str, **kwargs):
        self.nom = nom.lower()
        for k, v in kwargs.items():
            setattr(self, k.lower(), v.lower())


class BaliseContenu(Balise):
    def __init__(self, nom:str, contenu:str, **kwargs):
        Balise.__init__(self, nom, **kwargs)
        self.contenu = contenu.lower()
        






def main():
    pass



if __name__ == '__main__':
    main()

