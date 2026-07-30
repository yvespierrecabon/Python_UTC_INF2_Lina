class Region:

    horizon:int = 0

    def __init__(self,titre:str) -> None:
        self._titre:str = titre
        self._position:int = 0

    @property
    def titre(self) -> str:
        return self._titre

    @titre.setter
    def titre(self,val:str) -> None:
        self._titre = val

    @property
    def position(self) ->int:
        return self._position

    @position.setter
    def position(self,val:int) -> None:
        if val < 0:
            raise ValueError("Position doit être positif ou nul")
        self._position = val
        if self._position > Region.get_horizon():
            Region.set_horizon(self._position)

    def __str__(self) -> str:
        return f"{self.titre}"

    @classmethod
    def get_horizon(cls):
        return cls.horizon
    @classmethod
    def set_horizon(cls,val:int) -> None:
        if val > cls.horizon:
            cls.horizon = val




class Fichier:
    def __init__(self,titre:str, duree:int) -> None:
        self._titre:str = titre
        self._duree:int = duree

    def get_duree(self) -> int:
        return self._duree



class RegionAudio(Region):
    def __init__(self,titre:str, fichier:Fichier) -> None:
        super().__init__(titre)
        if not isinstance(fichier, Fichier):
            raise TypeError("Fichier inconnu")
        self._fichier = fichier
        self._debut = 0
        self._fin = 0

    def set_portion(self, debut:int,fin:int):
        if debut >= fin:
            raise ValueError("debut doit être inférieur à fin")
        if fin > self._fichier.get_duree():
            raise ValueError("fin ne peut pas dépasser la durée du fichier")
        self._debut = debut
        self._fin = fin
        if self.get_position_fin() > Region.get_horizon():
            Region.set_horizon(self.get_position_fin())



    def get_duree(self) -> int:
        return self._fin - self._debut

    def get_position_fin(self)->int:
        return self._position + self.get_duree()

    def __str__(self) -> str:
        return (f"{self.titre} durée : {self.get_duree()}")

    @Region.position.setter
    def position(self, val: int) -> None:
        super().position.__set__(self, val)  # Appelle le setter parent
        if self.get_position_fin() > Region.get_horizon():
            Region.set_horizon(self.get_position_fin())




