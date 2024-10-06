H, W = map(int, input().split())

L = []
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == "o":
            L.append([j, i])

print(abs(L[1][0]-L[0][0])+abs(L[1][1]-L[0][1]))
