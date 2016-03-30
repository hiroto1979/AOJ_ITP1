n = [int(i) for i in input().split()]

a = [0 for i1 in range(n[0])]
b = [0 for i1 in range(n[1])]

for i in range(n[0]):
    a[i] = [int(i) for i in input().split()]

for i in range(n[1]):
    b[i] = int(input())

for i in range(n[0]):
    c = 0
    for j in range(n[1]):
        c += a[i][j] *b[j]
    print(c)
