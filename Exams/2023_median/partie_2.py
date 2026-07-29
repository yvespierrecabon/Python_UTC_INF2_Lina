class Region:
    def __init__(self,titre:str) -> None:
        self._titre = titre
        self._position = 0

        @property
        def titre(self) -> str:
            return self._titre

        @titre.setter
        def titre(self,val:str) -> None:
            self._titre = val

        @property
        def position(self):
            return self._position

        @position.setter
        def position(self,val:int) -> None:
            if val < 0:
                raise ValueError("Position doit être positif ou nul")
            self._position = val

        def __str__(self) -> str:
            return f"{self.titre}"

class Fichier:
    def __init__(self,titre:str, duree:int) -> None:
        self._titre = titre
        self._duree = duree

        def get_duree(self) -> int:
            return self._duree



class RegionAudio(Region):
    def __init__(self,titre:str, fichier) -> None:
        super().__init__(titre)
        if not isinstance(fichier, Fichier):
            raise TypeError("Fichier inconnu")
        self._fichier = fichier
        self._debut = 0
        self._fin = 0

    def set_portion(self, debut:int,fin:int):
        if debut >= fin:
            raise ValueError("debut doit être superieur à fin")
        self._debut = debut
        self._fin = fin

    def get_duree(self) -> int:
        return self._fin - self._debut

    def get_position_fin(self):
        return position + self.get_duree()




