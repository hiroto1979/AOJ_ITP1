n = [int(i) for i in input().split()]
A = [[0 for i2 in range(n[1] + 1)]for i1 in range(n[0] + 1)]

for i in range(n[0]):
    row = [int(j) for j in input().split()]
    for k in range(n[1] + 1):
        if not k == n[1]:
            A[i][k] = row[k]
            A[i][n[1]] += A[i][k]
        A[n[0]][k] += A[i][k]

for i in range(n[0] + 1):
    for j in range(n[1] + 1):
        if j == n[1]:
            print(A[i][j], end='')
        else:
            print(A[i][j], '', end='')
    print()
