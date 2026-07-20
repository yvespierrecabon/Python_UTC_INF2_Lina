""" Q3 """
""" Q3-1 """
N = int(input("Entrez le nb de valeurs choisi :"))
moy = 0
for i in range(1, N + 1):
    texte = "Entrez la valeur " + str(i) + " : "
    moy += int(input(texte))
print("La moyenne vaut", moy / N)

N = int(input("Entrez le nb de valeurs choisi :"))
liste = []
for i in range(1, N + 1):
    texte = "Entrez la valeur " + str(i) + " : "
    liste.append(int(input(texte)))
print("La moyenne vaut", sum(liste) / N)
print(liste)

""" Q3-2 """
liste.sort()
print(liste[1:-1])
print("La moyenne centrée vaut", sum(liste[1:-1]) / (N - 2))

""" Q3-3"""
print("recherche de la valeur la plus proche de 0")
N = int(input("Entrez le nb de valeurs choisi :"))
liste = []
for i in range(1, N + 1):
    texte = "Entrez la valeur " + str(i) + " : "
    liste.append(int(input(texte)))
val_prox_0 =   liste[0]
diff = abs(liste[0])
for v in liste:
    if abs(v) < diff:
        diff = abs(v)
        val_prox_0 = v
    elif abs(v) == diff and v < val_prox_0:
        val_prox_0 = v

print("Valeur la plus proche de 0 :",val_prox_0)