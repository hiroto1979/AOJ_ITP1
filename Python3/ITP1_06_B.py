n = int(input())

cards = [[0 for i2 in range(14)] for i1 in range(4)]

for i in range(n):
    a = [i for i in input().split()]
    a1 = int(a[1])

    if(a[0] == 'S'):
        cards[0][a1] = 1
    if(a[0] == 'H'):
        cards[1][a1] = 1
    if(a[0] == 'C'):
        cards[2][a1] = 1
    if(a[0] == 'D'):
        cards[3][a1] = 1

for s in range(4):
    for r in range(1, 14):
        if(cards[s][r] == 1):
            continue
        if (s == 0):
            print("S "+ str(r))
        if (s == 1):
            print("H "+ str(r))
        if (s == 2):
            print("C "+ str(r))
        if (s == 3):
            print("D "+ str(r))
