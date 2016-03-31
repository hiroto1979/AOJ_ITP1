s = ""
while True:
    try:
        s += input().lower()
    except:
        break

for i in range(ord("a") , ord("z") + 1):
    print("{} : {}".format(chr(i), s.count(chr(i))))
