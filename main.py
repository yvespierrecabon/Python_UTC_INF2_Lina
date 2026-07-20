for i in range(1, 10):
    for j in range(1, 10-i):
        print(" ", end="")
    for j in range(0, i):
        print(i, end="")
    for j in range(0, i-1):
        print(i, end="")
    print()
