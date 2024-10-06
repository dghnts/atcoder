X = int(input())

N = -1
for i in range(X):
    N += 1
    if i*i > X:
        break

if X < 4:
    print(1)
    exit()

ans = 0

for i in range(2, N):
    j = 2
    while True:
        if i**j > X:
            ans = max(ans, i**(j-1))
            break
        else:
            j += 1

print(ans)
