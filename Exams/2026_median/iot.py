from random import randint

from pyasn1_modules.rfc2251 import AssertionValue


class EquipementIoT:
    def __init__(self, id:int, nom:str):
        self._id = id
        self._nom = nom
        self._protocoles = []

    @property
    def id(self):
        return self._id

    @property
    def nom(self):
        return self._nom

    @id.setter
    def id(self, id:int):
        self._id = id

    @nom.setter
    def nom(self, nom:str):
        self._nom = nom

    def ajouter_protocole(self, *args):
        for protocole in args:
            self._protocoles.append(protocole)

    def __str__(self):
       return f'EquipementIoT : ({self._id}, {self.nom})'


class CapteurIoT(EquipementIoT):
    def __init__(self, id:int, nom:str):
        super().__init__(id, nom)
        self._mesure = None

    def collecte(self):
        self._mesure = randint(0,100)

class ActionneurIoT(EquipementIoT):
    def __init__(self, id:int, nom:str, etat:str="OFF"):
        super().__init__(id, nom)
        self._etat = etat

    def collecte(self):
        return self._etat

class NoeudIot(EquipementIoT):
    def __init__(self, id:int, nom:str):
        super().__init__(id, nom)
        self._equipements=[]

    def connecter(self, e:'EquipementIoT') -> None:
        if isinstance(e, EquipementIoT) and list(set(self._protocoles) & set(e._protocoles)) :
            self._equipements.append(e)
            print(f'Connexion réussie pour {e}')
        else:
            print(f'Connexion impossible pour {e}')

    def collecte(self) -> dict:
        dico ={}
        for equipement in self._equipements:
            if (isinstance(equipement, CapteurIoT | ActionneurIoT)):
                dico[equipement.id] = equipement.collecte()
            elif isinstance(equipement, NoeudIot):
                dico[equipement.id] = equipement._equipements
        return dico


    def __add__(self, noeudIot:'NoeudIot'):
        noeudIoT_fusion = NoeudIot(self.id + noeudIot.id, self.nom + noeudIot.nom)
        noeudIoT_fusion._protocoles = list(set(self._protocoles + noeudIot._protocoles))
        noeudIoT_fusion._equipements = list(set(self._equipements + noeudIot._equipements))
        return noeudIoT_fusion



def main():
    protocoles = ["ble", "zigbee","wifi","uwb","loran"]
    thermometre = CapteurIoT(25,"Température")
    thermometre.ajouter_protocole("wifi")
    luninosite = CapteurIoT(2, "Luminosité")
    luninosite.ajouter_protocole("wifi")
    ventilo = ActionneurIoT(47, "Ventilateur")
    ventilo.ajouter_protocole("wifi")
    led = ActionneurIoT(10, "Lumière")
    # led.ajouter_protocole("wifi")
    noeud_a = NoeudIot(6, "routeur_hall")
    noeud_a.ajouter_protocole("wifi")

    noeud_b = NoeudIot(7, "routeur_salle")
    noeud_b.ajouter_protocole("ble", "zigbee", "wifi")
    noeud_b.connecter(thermometre)
    noeud_b.connecter(ventilo)
    noeud_b.connecter(led)
    noeud_b.connecter(luninosite)

    noeud_lab:NoeudIot = noeud_a + noeud_b
    noeud_lab.nom = "routeur labo"
    print(noeud_lab)
    print('Equipements connectés:')
    for id, collecte in noeud_lab.collecte().items():
        print('\t',id,collecte)








if __name__ == '__main__':
    main()
