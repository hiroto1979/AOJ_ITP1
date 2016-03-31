n = [int(i) for i in input().split()]

a = []
for i in range(n[0]):
    a.append([int(i) for i in input().split()])
b = []
for i in range(n[1]):
    b.append([int(j) for j in input().split()])

for i in range(n[0]):
    row = []
    for j in range(n[2]):
        c_ij = 0
        for k in range(n[1]):
            c_ij += a[i][k] * b[k][j]
        row.append(str(c_ij))
    print(" ".join(row))