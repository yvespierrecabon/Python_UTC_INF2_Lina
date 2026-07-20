"""Q1"""
"""
for i in range(1, 10):
    for j in range(1, 10-i):
        print(" ", end="")
    for j in range(0, i):
        print(i, end="")
    for j in range(0, i-1):
        print(i, end="")
    print()


for i in range(1, 10):
    for j in range(1, 10 - i):
        print(" ", end="")
    for j in range(0, 2*i-1):
        print(i, end="")
    print()

for i in range(1, 10):
    print(" "*(10-i), end="")
    for j in range(0, 2*i-1):
        print(i, end="")
    print()

for i in range(1, 10):
    print(" "*(10-i), end="")
    print(str(i)*(2*i-1), end="")
    print()

for i in range(1, 10):
    for j in range(1, 10 - i):
        print(" ", end="")
    for j in range(1,i+1):
        print(j, end="")
    for j in range(i-1,0,-1):
        print(j, end="")
    print()"""

"""Q2"""
"""
n1 = int(input('Entrez un entier positif :'))
n2 = int(input('Entrez un entier positif :'))

liste = [n for n in range(1, min(n1, n2)+1) if n1 % n == 0 and n2 % n == 0]
print(liste)
"""

""" Q3 """
""" Q3-1 """
N = int(input('Entrez le nb de valeurs choisi :'))
moy = 0
for i in range(1, N+1):
    texte = 'Entrez la valeur '+str(i)+' : '
    moy += int(input(texte))
print('La moyenne vaut',moy/N)

N = int(input('Entrez le nb de valeurs choisi :'))
liste = []
for i in range(1, N+1):
    texte = 'Entrez la valeur '+str(i)+' : '
    liste.append(int(input(texte)))
print('La moyenne vaut',sum(liste)/N)
print(liste)

""" Q3-2 """
liste.sort()
print(liste[1:-1])
print('La moyenne centrée vaut',sum(liste[1:-1])/(N-2))

""" Q3-3"""
print('Valeur la plus proche de 0 :')
i = 0
while i < len(liste) and  liste[i] < 0:
    i += 1

if i == len(liste):
    print(liste[-1])
else:
    if abs(liste[i-1]) <= abs(liste[i]):
        print(liste[i-1])
    else:
        print(liste[i])