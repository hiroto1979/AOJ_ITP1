while True:
    n = [int(i) for i in input().split()]
    if n[0] == 0 and n[1] == 0:
        break
    if n[0] <= n[1]:
        print(str(n[0]) + " " + str(n[1]))
    else:
        print(str(n[1]) + " " + str(n[0]))
