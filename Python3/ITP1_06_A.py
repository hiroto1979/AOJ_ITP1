n = int(input())
a = [int(i) for i in input().split()]
a1 = a[0]
a2 = reversed(a[1:])

for i in a2:
    print(i, end=" ")

print(a1)
