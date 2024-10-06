N = int(input())
A = [int(x) for x in input().split()]

count = []

for a in A:
    i = 0
    while True:
        if a % 2 != 0 or a == 0:
            count.append(i)
            break
        a //= 2
        i += 1

print(min(count))
