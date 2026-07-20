def somme_chiffre(n:int)->int:
    somme = 0
    while n>0:
        somme += n % 10
        n //=10
    return somme

print("124 : " ,somme_chiffre(124))
