B = int(input())

i = 1

while True:
    if i**i > B:
        print(-1)
        exit()
    if i**i == B:
        print(i)
        exit()
    else:
        i += 1
