X = int(input())

n = 0

while n*n <= 2*X:
    if 2*X <= n*(n+1):
        break
    else:
        n += 1

print(n)
