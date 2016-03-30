S = int(input())

s = S % 60;
M = (S - s) // 60;
m = M % 60;
h = (M - m) // 60;

print(str(h) + ":" + str(m) + ":" + str(s))
