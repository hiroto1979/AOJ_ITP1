n = [int(i) for i in input().split()]

d = n[0] // n[1]
r = n[0] % n[1]
f = n[0] / n[1]

print('%s %s %.5f' % (d, r, f))