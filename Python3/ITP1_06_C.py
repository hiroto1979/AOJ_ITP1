n = int(input())

count = [[[0 for i3 in range(11)] for i2 in range(4)] for i1 in range(5)]

for i in range(n):
    a = [int(i) for i in input().split()]
    count[a[0]][a[1]][a[2]] += a[3]

for r0 in range(1, 5):
    for r1 in range(1, 4):
        for r2 in range(1, 11):
            print(" " + str(count[r0][r1][r2]), end="")
        print()
    if(r0 < 4):
        print("####################")
