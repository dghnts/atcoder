n = int(input())
b = [int(x) for x in input().split()]

res = []

for i in range(n):
    pivot = -1
    for j in range(len(b)-1, -1, -1):
        if b[j] == j+1:
            pivot = j
            break
    if pivot == -1:
        print(-1)
        exit()

    res.append(pivot+1)
    b.pop(j)

res.reverse()

for i in range(n):
    print(res[i])
