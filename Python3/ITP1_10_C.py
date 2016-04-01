import math

while True:
    n = int(input())
    if n == 0:
        break

    points = [float(i) for i in input().split()]
    m = sum(points) / n

    tmp = 0.0
    for i in range(n):
        tmp += (points[i] - m) ** 2

    a = math.sqrt(tmp/n)
    print(a)