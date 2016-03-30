n = [int(i) for i in input().split()]

if 0 <= n[2] - n[4] and n[2] + n[4] <= n[0] and 0 <= n[3] - n[4] and n[3] + n[4] <= n[1]:
    print("Yes")
else:
    print("No")
