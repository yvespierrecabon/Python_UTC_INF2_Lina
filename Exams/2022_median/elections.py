import os
from typing import List, Dict

def creer_dictionnaire_candidats(liste:List[str]) -> Dict[str, int]:
    dictionnaire_candidats = {'Nul':0, 'Blanc':0}
    for candidat in liste:
        dictionnaire_candidats[candidat] = 0
    return dictionnaire_candidats

def lancer_depouillement(dico:Dict[str,int]) -> None:
    continuer = True
    while continuer:
        nom_candidat = input("Nom du candidat : ")
        if nom_candidat in dico:
            dico[nom_candidat] += 1
        elif nom_candidat.strip().lower() =='blanc':
            dico['Blanc'] += 1
        elif nom_candidat not in dico:
            dico['Nul'] += 1
        suite = input('Continuer ? o / n')
        if suite == 'n':
            continuer = False

def enregistrer_resultats(ville:str, num_bureau:int, dico:Dict[str,int]) -> None:
    fichier = ville+'_'+str(num_bureau)+'.txt'
    if fichier in os.listdir():
        raise FileExistsError('Le fichier existe déjà')
    else:
        with open(fichier, 'w') as file:
            for candidat, nb_voix in dico.items():
                if candidat not in ('Nul','Blanc'):
                    file.write(candidat+' | '+str(nb_voix)+'\n')
            file.write('Nul | '+str(dico['Nul'])+'\n')
            file.write('Blanc | '+str(dico['Blanc']))

def nombre_votants(dico:Dict[str,int]) -> tuple:
    total_exprimes = 0
    total_nuls= dico['Nul']
    total_blancs= dico['Blanc']
    for candidat, nb_votant in dico.items():
        if candidat not in ('Nul','Blanc'):
            total_exprimes += dico[candidat]
    return total_exprimes, total_nuls, total_blancs

def afficher_resultats(dico:Dict[str,int]) -> None:
    total_exprimes, total_nuls, total_blancs= nombre_votants(dico)
    total_votants = total_exprimes + total_blancs+total_nuls
    print(f"Total votants = {total_votants}")
    print(f"Total exprimés = {(100*total_exprimes/total_votants):.2f}% ({total_exprimes})")
    print(f"Blancs = {(100*total_blancs/total_votants):.2f}% ({total_blancs})")
    print(f"Nuls = {(100*total_nuls/total_votants):.2f}% ({total_nuls})")
    for candidat, nb_votant in dico.items():
        if candidat not in ('Nul','Blanc'):
            print(f"{candidat} = {(100*dico[candidat]/total_exprimes):.2f}% ({dico[candidat]})")




def main():
    dico_candidats = creer_dictionnaire_candidats(['yves', 'corine', 'sedra'])
    lancer_depouillement(dico_candidats)
    afficher_resultats(dico_candidats)
    enregistrer_resultats('Compiègne',19, dico_candidats)




if __name__ == '__main__':
    main()