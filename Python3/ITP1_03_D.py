n = [int(i) for i in input().split()]

s = 0
for i in range(n[0], n[1]+1):
    if n[2] % i == 0:
        s += 1
print(s)