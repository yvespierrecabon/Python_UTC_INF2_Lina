def somme_chiffres(n:int)->int:
    somme = 0
    while n>0:
        somme += n % 10
        n //=10
    return somme

def nombre_chiffres(n:int)->int:
    return len(str(n))

def separe_nombre(n:int)->tuple:
    str_nb = str(n)
    sep = len(str_nb)//2
    return int(str_nb[:sep]),int(str_nb[sep:])

def est_couicable(n:int)->int:
    nb1,nb2 = separe_nombre(n)
    return nombre_chiffres(nb1) == nombre_chiffres(nb2)

def somme_chiffres_rec(n:int)->int:
    if n<10:
        return n
    return n%10 + somme_chiffres_rec(n//10)

print("124\nSomme des chiffres :" ,somme_chiffres(1245678))
print("124\nNombre de chiffres :" ,nombre_chiffres(1245678))
print("124567\nSépare en 2 :" ,separe_nombre(12345678))
print("124\nSomme des chiffres :" ,somme_chiffres_rec(1245678))
