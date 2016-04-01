import math

a, b, C = [float(i) for i in input().split()]
C = math.pi * C / 180

S = a * b * math.sin(C) / 2.0
print(S)
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))
print(L)
h = b * math.sin(C)
print(h)
