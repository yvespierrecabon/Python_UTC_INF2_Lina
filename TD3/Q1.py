import fcts_carre_magique as cm

def sont_carres(*args) -> None:
    for carre in args:
        print(carre)
        print(f"Carré magique  : {cm.est_carre_magique(carre)}")
        print(f"Carré magique normal : {cm.est_carre_magique_normal(carre)}")


def main():
    mat1 = [[21, 7, 17], [11, 15, 19], [13, 23, 9]]
    mat2 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    sont_carres(mat1, mat2)


if __name__ == "__main__":
    main()
