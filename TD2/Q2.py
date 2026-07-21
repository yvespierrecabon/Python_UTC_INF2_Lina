from typing import *

def somme_ligne(mat:list, i:int)->int:
    return sum(mat[i][:])

def somme_colonne(mat:list, i:int)->int:
    return sum(mat[:][i])

def somme_diag_1(mat:list)->int:
    return sum([mat[i][i] for i in range(0,len(mat))])

def somme_diag_2(mat:list)->int:
    return sum([mat[len(mat) -1 -i][i] for i in range(0,len(mat))])

def magique(mat:list)->bool:
    dim = len(mat)
    somme = somme_ligne(mat,0)


    for i in range(dim):
        if somme_ligne(mat,i) !=somme:
            return False
        if  somme_colonne(mat,i) !=somme:
            return False
    if somme_diag_1(mat) !=somme:
        return False
    if somme_diag_2(mat) !=somme:
        return False
    return True


def main():
    mat1 = [[21,7,17],[11,15,19],[13,23,9]]
    print(f"somme ligne 1 : {somme_ligne(mat1,1)}")
    print(f"somme colonne 1 : {somme_colonne(mat1,1)}")
    print(f"somme diag 1 : {somme_diag_1(mat1)}")
    print(f"somme diag 2 : {somme_diag_2(mat1)}")
    print(f"magique : {magique(mat1)}")

if __name__== "__main__":
    main()