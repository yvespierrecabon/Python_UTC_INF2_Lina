inf2 = {
    "Pierre BERTRAND": 13,
    "Géraldine LECORRE": 17,
    "Rémi BRAUN": 9,
    "Fanny FORSTER": 15,
    "Nina PIERRY": 8,
    "Franck DUPUIS": 14,
    "Thomas NISSAR": 16,
    "Alou SAMOE": 12,
    "Samia CHOKY": 13,
    "Suzanne BRUNNEAU": 15,
    "Philippe RIVES": 9,
    "Youssef BARAOUI": 14,
    "Jeanne WALLET": 10,
    "Violette ROMBOURG": 12,
    "Gaspard LAVAUD": 13,
    "Maria LABOSSE": 7,
    "Basile DUMOULIN": 12,
    "Chaowei XU": 15,
    "Minh NGUYEN": 9,
    "Morgane VERNIER": 17,
}


def get_moyenne_dico(dico:dict)->float:
    if not dico:
        return 0.0
    return sum(dico.values())/len(dico)


etudiants_admis = {}
etudiants_non_admis = {}

for etudiant,moyenne in inf2.items():
    if moyenne >= 10:
        etudiants_admis[etudiant] = moyenne
    else:
        etudiants_non_admis[etudiant] = moyenne

print("etudiants admis")
print(etudiants_admis)
print(f"Moyenne : {get_moyenne_dico(etudiants_admis):.2f}")
print(etudiants_non_admis)
print('Moyenne : ',get_moyenne_dico(etudiants_non_admis))