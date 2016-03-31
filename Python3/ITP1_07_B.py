while True:
    a = [int(i) for i in input().split()]
    if a[0] == 0 and a[1] == 0:
        break
    s = 0
    for i in range(1, a[0]-1):
        for j in range(i+1, a[0]):
            for k in range(j+1, a[0]+1):
                if i + j + k == a[1]:
                    s += 1
    print(s)
