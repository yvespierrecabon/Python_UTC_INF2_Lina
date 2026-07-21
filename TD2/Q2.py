from typing import List


def somme_ligne(mat: List[List[int]], i: int) -> int:
    return sum(mat[i])


def somme_colonne(mat: List[List[int]], j: int) -> int:
    return sum(row[j] for row in mat)


def somme_diag_1(mat: List[List[int]]) -> int:
    return sum([mat[i][i] for i in range(0, len(mat))])


def somme_diag_2(mat: List[List[int]]) -> int:
    return sum([mat[len(mat) - 1 - i][i] for i in range(0, len(mat))])


def est_carre_magique(mat: List[List[int]]) -> bool:
    dim = len(mat)
    somme = somme_ligne(mat, 0)
    for i in range(dim):
        if somme_ligne(mat, i) != somme:
            return False
        if somme_colonne(mat, i) != somme:
            return False
    if somme_diag_1(mat) != somme:
        return False
    if somme_diag_2(mat) != somme:
        return False
    return True


def est_carre_magique_normal(mat: List[List[int]]) -> bool:
    set_chiffres_attendus = set(i for i in range(1, 1+ len(mat) ** 2))
    set_chiffres_trouves = set()

    for ligne in mat:
        for chiffre in ligne:
            if chiffre not in set_chiffres_attendus:
                return False
            (set_chiffres_trouves.add(chiffre))
    return set_chiffres_trouves == set_chiffres_attendus and est_carre_magique(mat)


def main():
    mat1 = [[21, 7, 17], [11, 15, 19], [13, 23, 9]]
    print(f"somme ligne 1 : {somme_ligne(mat1, 1)}")
    print(f"somme colonne 1 : {somme_colonne(mat1, 1)}")
    print(f"somme diag 1 : {somme_diag_1(mat1)}")
    print(f"somme diag 2 : {somme_diag_2(mat1)}")
    print(f"magique : {est_carre_magique(mat1)}")

    print(
        f"Carré magique normal : {est_carre_magique_normal([[8, 1, 6], [3, 5, 7], [4, 9, 2]])}"
    )
    print(
        f"Carré magique normal : {est_carre_magique_normal([[21, 7, 17], [11, 15, 19], [13, 23, 9]])}"
    )


if __name__ == "__main__":
    main()
