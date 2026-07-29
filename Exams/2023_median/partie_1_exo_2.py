from typing import List


def moyenne(liste:List[int]) -> float:
    return sum(liste)/len(liste)




def ajouter_train(numero, statut, **kwargs):
    statuts = ('ANNULE', 'EN_RETARD','A_L_HEURE')
    retard = 0
    if statut not in statuts:
        raise ValueError(f"Erreur de statut : {statut}")
    if statut == 'EN_RETARD':
        if 'retard' not in kwargs:
            raise ValueError(f"retard manquant")
        retard = kwargs['retard']
    nom_fichier ='trains.txt'
    if 'nom_fichier' in kwargs:
        nom_fichier = kwargs['nom_fichier']
    with open(nom_fichier,'a') as f:
        if statut == 'ANNULE':
            print(f"TER{numero:03d}|{statut}", file=f)
        else:
            print(f"TER{numero:03d}|{statut}|{retard}", file=f)

def main():
    ajouter_train(1, 'ANNULE')
    ajouter_train(2, 'A_L_HEURE')
    ajouter_train(3, 'EN_RETARD', retard=15)



if __name__ == "__main__":
    main()