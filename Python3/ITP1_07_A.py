while True:
    a = [int(i) for i in input().split()]
    if a[0] == -1 and a[1] == -1 and a[2] == -1:
        break

    if a[0] == -1 or a[1] == -1 or (a[0] + a[1] < 30):
        print('F')
    elif 80 <= a[0] + a[1]:
        print('A')
    elif 65 <= a[0] + a[1] and a[0] + a[1] < 80:
        print('B')
    elif 50 <= a[0] + a[1] and a[0] + a[1] < 65:
        print('C')
    elif (30 <= a[0] + a[1] and a[0] + a[1] < 50) and 50 <= a[2]:
        print('C')
    else:
        print('D')
