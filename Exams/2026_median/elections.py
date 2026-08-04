from collections import Counter

def detection_fraude(fonction):
    def wrapper(*args):
        if len(args) >= 1:
            bureau = args[0]
            if sum(bureau['votes'].values()) > bureau['inscrits']:
                print(f"fraude détectée au bureau {bureau['numero']}")
                return 0
            else:
                return fonction(*args)
        else:
            pass
    return wrapper


@detection_fraude
def ajoute_bureau(bureau:dict,ville:list) -> None:
    bureaux_enregistres = [bureau['numero'] for bureau in ville]
    print(bureaux_enregistres)
    if bureau['numero'] not in bureaux_enregistres:
        ville.append(bureau)
    else:
        print(f"résultat du bureau {bureau['numero']} déjà saisis")

def ajoute_bureaux(*args, ville:list) -> None:
    for arg in args:
        ajoute_bureau(arg, ville)

@detection_fraude
def taux_participation(bureau:dict) -> float:
    return 100*sum(bureau['votes'].values())/bureau['inscrits']

def meilleur_taux(ville:list) -> str:
    taux_participation_ = [(bureau['numero'], taux_participation(bureau)) for bureau in ville]
    return max(taux_participation_, key=lambda x: x[1])[0]



def total_candidats(ville:list) -> dict:
    total_candidats = Counter()
    for bureau in ville:
        for candidat, score in bureau['votes'].items():
            total_candidats[candidat] += score
    return dict(total_candidats)

def candidats_second_tour(ville:list, seuil:float) -> list:
    total_candidats_ = total_candidats(ville)
    total_votes = sum(total_candidats_.values())
    return [candidat for candidat,score in total_candidats_.items() if 100*score/total_votes > seuil]



def main():
    ville =[]

    bureau_1 = {"numero":1, "inscrits":500, "votes":{"Marinier":120, "Blaque":95, "Foret":60}}
    bureau_8 = {"numero":8, "inscrits":400, "votes":{"Marinier":80, "Blaque":110, "Foret":70}}
    bureau_15 = {"numero":15, "inscrits":760, "votes":{"Marinier":150, "Blaque":130, "Foret":90}}
    bureau_4 = {"numero":4, "inscrits":550, "votes":{"Marinier":90, "Blaque":85, "Foret":100}}
    bureau_9 = {"numero":9, "inscrits":380, "votes":{"Marinier":70, "Blaque":60, "Foret":80}}
    ajoute_bureaux(bureau_1,bureau_4,bureau_8, bureau_9,bureau_15, ville=ville)
    """ajoute_bureau(bureau_1,ville)
    ajoute_bureau(bureau_8,ville)
    ajoute_bureau(bureau_15,ville)
    ajoute_bureau(bureau_4,ville)
    ajoute_bureau(bureau_9,ville)
    ajoute_bureau(bureau_9,ville)"""
    for bureau in ville:
        print(bureau)


    print(total_candidats(ville))
    print('Meilleur taux de participation :',meilleur_taux(ville))
    print(candidats_second_tour(ville, 32))






if __name__ == "__main__":
    main()

