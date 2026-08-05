from random import randint


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
            if protocole not in self._protocoles:
                self._protocoles.append(protocole)

    def __str__(self):
       return f'{self._id}, {self._nom}'


class CapteurIoT(EquipementIoT):
    def __init__(self, id:int, nom:str):
        super().__init__(id, nom)
        self._mesure = None

    def collecte(self):
        self._mesure = randint(0,100)
        return self._mesure

class ActionneurIoT(EquipementIoT):
    def __init__(self, id:int, nom:str, etat:str="OFF"):
        super().__init__(id, nom)
        self._etat = etat

    def collecte(self):
        return self._etat

class NoeudIoT(EquipementIoT):
    def __init__(self, id:int, nom:str):
        super().__init__(id, nom)
        self._equipements=[]

    def connecter(self, e:'EquipementIoT') -> None:
        if isinstance(e, EquipementIoT) and set(self._protocoles) & set(e._protocoles) :
            self._equipements.append(e)
            print(f'Connexion réussie pour {e}')
        else:
            print(f'Connexion impossible pour {e}')

    def collecte(self) -> dict:
        dico ={}
        for equipement in self._equipements:
            if (isinstance(equipement, (CapteurIoT , ActionneurIoT))):
                dico[equipement.id] = equipement.collecte()
            elif isinstance(equipement, NoeudIoT):
                dico[equipement.id] = equipement.collecte()
        return dico


    def __add__(self, noeudIoT:'NoeudIoT'):
        noeudIoT_fusion = NoeudIoT(self.id + noeudIoT.id, self.nom + noeudIoT.nom)
        noeudIoT_fusion._protocoles = list(set(self._protocoles + noeudIoT._protocoles))
        fusion_equipements = self._equipements + noeudIoT._equipements
        for equipement in fusion_equipements:
            if equipement.id not in [eq.id for eq in noeudIoT_fusion._equipements]:
                noeudIoT_fusion._equipements.append(equipement)
        return noeudIoT_fusion



def main():
    protocoles = ["ble", "zigbee","wifi","uwb","loran"]
    thermometre = CapteurIoT(25,"Température")
    thermometre.ajouter_protocole("wifi")
    luminosite = CapteurIoT(2, "Luminosité")
    luminosite.ajouter_protocole("wifi")
    ventilo = ActionneurIoT(47, "Ventilateur")
    ventilo.ajouter_protocole("wifi")
    led = ActionneurIoT(10, "Lumière")
    # led.ajouter_protocole("wifi")
    noeud_a = NoeudIoT(6, "routeur_hall")
    noeud_a.ajouter_protocole("wifi")

    noeud_b = NoeudIoT(7, "routeur_salle")
    noeud_b.ajouter_protocole("ble", "zigbee", "wifi")
    noeud_b.connecter(thermometre)
    noeud_b.connecter(ventilo)
    noeud_b.connecter(led)
    noeud_b.connecter(luminosite)

    noeud_lab:NoeudIoT = noeud_a + noeud_b
    noeud_lab.nom = "routeur_labo"
    print(noeud_lab)
    print('Equipements connectés:')
    for id, collecte in noeud_lab.collecte().items():
        print('\t',id,collecte)








if __name__ == '__main__':
    main()
