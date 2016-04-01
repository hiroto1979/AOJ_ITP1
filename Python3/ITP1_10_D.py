import math

n = int(input())
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

# P = 1 のケース 
p_1 = 0
for i in range(n):
    p_1 += math.fabs(x[i] - y[i])
print(p_1)

# P = 2 のケース 
tmp = 0
for i in range(n):
    tmp += (x[i] - y[i]) ** 2
    p_2 = math.sqrt(tmp)
print(p_2)

# P = 3 のケース 
tmp = 0
for i in range(n):
    tmp += math.fabs((x[i] - y[i]) ** 3)
    p_3 = tmp ** (1/3)
print(p_3)

# P = inf のケース 
p_inf = math.fabs(x[0] - y[0])
for i in range(n):
    tmp = math.fabs(x[i] - y[i])
    if p_inf < tmp:
        p_inf = tmp
print(p_inf)
