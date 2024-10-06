H,W = map(int,input().split())

B = [[0 for _ in range(H)] for _ in range(W)]

for i in range(H):
    col = [int(x) for x in input().split()]
    for j in range(W):
        B[j][i] = col[j]

for i in range(W):
    print(*B[i]) 