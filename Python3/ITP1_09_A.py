W = input().lower()

cnt = 0
while True:
    T = input()
    if T == "END_OF_TEXT":
        break
    text = T.lower().split()
    cnt += text.count(W)

print(cnt)
