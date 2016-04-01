sr = input()
n = int(input())

for i in range(n):
    command = input().split()
    a1 = int(command[1])
    a2 = int(command[2]) + 1

    if command[0] == "print":
        print(sr[a1:a2])
    if command[0] == "reverse":
        sr = sr[:a1] + sr[a1:a2][::-1] + sr[a2:]
        # print(sr)
    if command[0] == "replace":
        sr = sr[:a1] + command[3] + sr[a2:]
        # print(sr)
