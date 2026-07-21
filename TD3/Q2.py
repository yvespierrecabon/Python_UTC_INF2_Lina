

def calculer_polynome(x, **kwargs)->float:
    poly = 0
    for key, value in kwargs.items():
        if key == 'a':
            poly += value*(x**3)
        elif key == 'b':
            poly += value*(x**2)
        elif key == 'c':
            poly += value*x
        elif key == 'd':
            poly += value
    return poly

def calculer_polynome_2(*args, **kwargs)->float:
    res = []
    for x in args:
        poly = 0
        for key, value in kwargs.items():
            if key == 'a':
                poly += value*(x**3)
            elif key == 'b':
                poly += value*(x**2)
            elif key == 'c':
                poly += value*x
            elif key == 'd':
                poly += value
        res.append(poly)
    return res


def main():
    print(calculer_polynome(3, a=1, b=2, c=3, d=4))
    print(calculer_polynome_2(0,1,2,3,4,5, a=1, b=2, c=3, d=4))



if __name__ == "__main__":
    main()

