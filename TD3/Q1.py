import fcts_carre_magique as cm


def test_carres(*args) -> None:
    nb_carres = args[0]
    for carre in args[1:]:
        print(carre)
        print(f"Carré magique normal : {cm.est_carre_magique_normal(carre)}")
        print(f"Carré magique normal : {cm.est_carre_magique_normal(carre)}")


def main():
    mat1 = [[21, 7, 17], [11, 15, 19], [13, 23, 9]]
    mat2 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    mat3 = [[21, 7, 17], [11, 15, 19], [13, 23, 9]]
    test_carres((mat1, mat2, mat3))


if __name__ == "__main__":
    main()
