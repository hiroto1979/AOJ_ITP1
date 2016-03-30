n = [int(i) for i in input().split()]

if n[0] < n[1]:
    print("a < b")
elif n[0] == n[1]:
    print("a == b")
else:
    print("a > b")
