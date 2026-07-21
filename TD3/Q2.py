from typing import List

def calculer_polynome(x, **kwargs)->float:
    poly = 0
    puissance = {"a": 3, "b": 2, "c": 1, "d": 0}
    for key, value in kwargs.items():
        if key not in puissance:
            raise ValueError(f"Coefficient invalide : {key}")
        else:
            poly += value*(x**puissance[key])
    return poly

def calculer_polynome_2(*args, **kwargs)->List[float]:
    res = []
    for x in args:
        poly = 0
        puissance =  {'a': 3, 'b': 2, 'c': 1, 'd': 0}
        for key, value in kwargs.items():
            if key not in puissance:
                raise ValueError(f"Coefficient invalide : {key}")
            else:
                poly += value*(x**puissance[key])
        res.append(poly)
    return res


def main():
    print(calculer_polynome(3, a=1, b=2, c=3, d=4))
    print(calculer_polynome_2(0,1,2,3,4,5, a=1, b=2, c=3, d=4))



if __name__ == "__main__":
    main()

