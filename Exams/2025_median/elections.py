def verifier_vote(fonction):
    def wrapper(scrutin: dict, candidats: list, identifiant: str, vote: list):
        if identifiant in scrutin.keys() or set(candidats) != set(vote):
            raise ValueError("vote non valide")
        return fonction(scrutin, candidats, identifiant, vote)

    return wrapper


@verifier_vote
def a_vote(scrutin: dict, candidats: list, identifiant: str, vote: list):
    scrutin[identifiant] = vote


def calcul_scores(scrutin: dict, candidats: list):
    liste_vote_preference = []
    for choix in scrutin.values():
        liste_vote_preference.append(choix[0])
    vote_preference = {}
    for candidat in candidats:
        vote_preference[candidat] = liste_vote_preference.count(candidat)
    return vote_preference


def majorite_abolue(scores: dict):
    votes = sum(scores.values())
    for score in scores.values():
        if 2 * score > votes:
            return True
    return False


def dernier_candidat(scores: dict):
    return min(scores, key=scores.get)


def determine_gagnant(scrutin: dict, candidats: list):
    scores = calcul_scores(scrutin, candidats)
    while not majorite_abolue(scores):
        dernier_candidat_ = dernier_candidat(scores)
        # print("Suppression de ",dernier_candidat_)
        for k, v in scrutin.items():
            v.remove(dernier_candidat_)
        candidats.remove(dernier_candidat_)
        # print("Scrutin",scrutin)
        scores = calcul_scores(scrutin, candidats)
    dernier_candidat_ = dernier_candidat(scores)
    scores.pop(dernier_candidat_, None)
    return list(scores.keys())[0]


def main():
    scrutin_1 = {}
    candidats = ["lapin", "Lion", "Renard"]

    a_vote(scrutin_1, candidats, "1", ["lapin", "Lion", "Renard"])
    a_vote(scrutin_1, candidats, "2", ["lapin", "Lion", "Renard"])
    a_vote(scrutin_1, candidats, "3", ["lapin", "Lion", "Renard"])
    a_vote(scrutin_1, candidats, "3", ["lapin", "Lion", "Renard"])
    a_vote(scrutin_1, candidats, "5", ["lapin", "Lion", "Renard"])

    a_vote(scrutin_1, candidats, "6", ["Renard", "lapin", "Lion"])
    a_vote(scrutin_1, candidats, "7", ["Renard", "lapin", "Lion"])
    a_vote(scrutin_1, candidats, "8", ["Renard", "lapin", "Lion"])
    a_vote(scrutin_1, candidats, "9", ["Renard", "lapin", "Lion"])

    a_vote(scrutin_1, candidats, "10", ["Lion", "Renard", "lapin"])
    a_vote(scrutin_1, candidats, "11", ["Lion", "Renard", "lapin"])

    scores = calcul_scores(scrutin_1, candidats)

    print(scores)
    print(majorite_abolue(scores))
    print(dernier_candidat(scores))
    print(determine_gagnant(scrutin_1, candidats))


if __name__ == "__main__":
    main()
