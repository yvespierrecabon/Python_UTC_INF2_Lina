from typing import Tuple

def nombre(fonction):
    def wrapper(nb):
        if  isinstance(nb,str) and isinstance(int(nb),int):
            try:
                nb = int(nb)
            except ValueError:
                nb = 0
        else:
            nb = 0
        return fonction(nb)
    return wrapper

@nombre
def somme_chiffres(n:int)->int:
    n = abs(n)
    somme = 0
    while n>0:
        somme += n % 10
        n //=10
    return somme

@nombre
def nombre_chiffres(n:int)->int:
    return len(str(n))

@nombre
def separe_nombre(n:int)->Tuple[int,int]:
    str_nb = str(n)
    sep = (len(str_nb)+1)//2
    return int(str_nb[:sep]),int(str_nb[sep:])

@nombre
def est_couicable(n)->bool:
    if nombre_chiffres(n)%2 != 0:
        return False
    nb1,nb2 = separe_nombre(n)
    return somme_chiffres(nb1) == somme_chiffres(nb2)
@nombre
def somme_chiffres_rec(n:int)->int:
    n=abs(n)
    if n<10:
        return n
    return n%10 + somme_chiffres_rec(n//10)






def main():
    print("Somme des chiffres :" ,somme_chiffres(1245678))
    print("Nombre de chiffres :" ,nombre_chiffres(1245678))
    print("Sépare en 2 :" ,separe_nombre(12345678))
    print("Somme des chiffres :" ,somme_chiffres_rec(1245678))

    n = input("Entrez un nombre : ")
    if est_couicable(n):
        print(f"{n} est couicable !")
    else:
        print(f"{n} n'est pas couicable.")



if __name__== "__main__":
    main()