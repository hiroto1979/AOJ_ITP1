while True:
    data = input()
    if '?' in data:
        break
    print(eval(data.replace('/','//')))
