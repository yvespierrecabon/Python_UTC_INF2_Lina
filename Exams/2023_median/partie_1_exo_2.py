from typing import List, Dict


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

def parser_train(ligne:str)->Dict[str, str]:
    ligne = ligne[:-1]
    valeur = ligne.split('|')
    dico = {}
    dico['nom'] = valeur[0]
    dico['statut'] = valeur[1]
    if len(valeur) == 3:
        dico['retard'] = int(valeur[2])
    return dico
    
def lire_retard(nom_fichier:str):
    dico ={}
    with open(nom_fichier,'r') as f:
        for ligne in f:
            dico_ligne = parser_train(ligne)
            print(dico_ligne)
            if dico_ligne['statut'] != 'ANNULE':
                if dico_ligne['nom'] in dico:
                    dico[dico_ligne['nom']].append(dico_ligne['retard'])
                else:
                    dico[dico_ligne['nom']] = [dico_ligne['retard']]
    return dico

def trop_en_retard(dico:dict) ->None:
    for train, retards in dico.items():
        if moyenne(retards) > 5:
            print(f"Trop en retard: {train} ({moyenne(retards):.2f} minutes))")

def main():
    ajouter_train(1, 'ANNULE')
    ajouter_train(2, 'A_L_HEURE')
    ajouter_train(3, 'EN_RETARD', retard=15)
    print(parser_train("TER003|EN_RETARD|15\n"))
    print(parser_train("TER001|ANNULE\n"))
    print(parser_train("TER002|A_L_HEURE|0\n"))
    retards= lire_retard('trains.txt')
    print(retards)
    trop_en_retard(retards)



if __name__ == "__main__":
    main()