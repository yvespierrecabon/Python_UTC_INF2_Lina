
"""Q2"""

n1 = int(input('Entrez un entier positif :'))
n2 = int(input('Entrez un entier positif :'))

liste = [n for n in range(1, min(n1, n2)+1) if n1 % n == 0 and n2 % n == 0]
print(liste)

