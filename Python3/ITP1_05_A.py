while True:
    n = [int(i) for i in input().split()]
    if n[0] == 0 and n[1] == 0:
        break
    for i in range(0, n[0]):
        for j in range(0, n[1]):
            print("#", end=""),
        print()
    print()
