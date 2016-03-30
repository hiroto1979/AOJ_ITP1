n = int(input())
lst = [int(i) for i in input().split()]

a = min(lst)
b = max(lst)
c = sum(lst)

print("{0} {1} {2}".format(a, b, c))