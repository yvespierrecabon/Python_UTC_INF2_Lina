from typing import List, Dict

def creer_dictionnaire_candidats(liste:List[str]) -> Dict[str, int]:
    dictionnaire_candidats = {'Nul':0, 'Blanc':0}
    for candidat in liste:
        dictionnaire_candidats[candidat] = 0
    return dictionnaire_candidats



def main():
    pass




 if __name__ == '__main__':
    main()