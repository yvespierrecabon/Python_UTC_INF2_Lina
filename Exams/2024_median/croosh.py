def creer_evt(prix: float, nb_places_max: int) -> dict:
    if not (isinstance(nb_places_max, int) and nb_places_max > 0):
        raise TypeError("nb_places_max must be an positive integer")
    return {"prix": prix, "participants": list(), "nb_places_max": nb_places_max}

def retirer_evt(dico_tous_evts:dict, evt:str) -> bool:
    if evt not in dico_tous_evts.keys():
        return False
    else:
        dico_tous_evts.pop(evt)
        return True

def ajouter_participants(dico_tous_evts:dict, evt:str, login:str) -> bool:
    if evt not in dico_tous_evts.keys():
        raise TypeError("Event not recognized")
    if not (' ' not in login and len(login) < 8):
        raise TypeError("login incorrect")
    if len(dico_tous_evts[evt]) == dico_tous_evts[evt]['nb_places_max']:
        raise EventFullError("Event full")
    dico_tous_evts[evt]["participants"].append(login)
    return True

def stats_ventes(dico_tous_evts:dict) -> dict:
    dico = {}
    for evt_nom, evt_dico in dico_tous_evts.items():
        dico[evt_nom] = evt_dico["prix"] * len(evt_dico["participants"])
    return dico





def main():

    dico_evts = {}
    evt1 = creer_evt(prix=5, nb_places_max=3)
    evt2 = creer_evt(prix=10, nb_places_max=4)
    evt3 = creer_evt(prix=20, nb_places_max=5)

    dico_evts['evt1'] = evt1
    dico_evts['evt2'] = evt2
    dico_evts['evt3'] = evt3

    retirer_evt(dico_evts, 'evt3')
    ajouter_participants(dico_evts, 'evt1', 'yves')
    ajouter_participants(dico_evts, 'evt1', 'Lina')
    ajouter_participants(dico_evts, 'evt1', 'joshua')
    ajouter_participants(dico_evts, 'evt1', 'Sedra')









if __name__ == "__main__":
    main()
