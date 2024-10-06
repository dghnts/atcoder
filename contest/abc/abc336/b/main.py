N = int(input())

count = 0

while True:
    if N % 2 == 1:
        break

    count += 1

    N = N//2

print(count)
