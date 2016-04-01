while True:
    word = input()
    if word == "-":
        break

    n = int(input())

    for i in range(n):
        j = int(input())
        word = word[j:] + word[:j]
    print(word)