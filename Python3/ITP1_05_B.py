while True:
    n = [int(i) for i in input().split()]
    if n[0] == 0 and n[1] == 0:
        break
    for j in range(0, n[1]):
        print("#", end="")
    print()
    for i in range(1, n[0]-1):
        print("#", end=""),
        for j in range(1, n[1]-1):
            print(".", end="")
        print("#")
    for j in range(0, n[1]):
        print("#", end="")
    print()
    print()

