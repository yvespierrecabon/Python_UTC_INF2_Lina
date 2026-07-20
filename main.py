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
n1 = int(input('Entrez un entier positif :'))
n2 = int(input('Entrez un entier positif :'))

liste = [n for n in range(1, min(n1, n2)+1) if n1 % n == 0 and n2 % n == 0]
print(liste)