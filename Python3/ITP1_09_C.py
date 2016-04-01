n = int(input())

points= [0, 0]
for i in range(n):
    words = input().split()
    if words[0] < words[1]:
        points[1] += 3
    elif words[0] == words[1]:
        points[0] += 1
        points[1] += 1
    elif words[1] < words[0]:
        points[0] += 3

print(str(points[0]) + " " + str(points[1]))
