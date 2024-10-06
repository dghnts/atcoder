H,W = map(int,input().split())

S = []
T = [] 

U = [[] for _ in range(W)]
V = [[] for _ in range(W)]

for i in range(H):
    S.append(list(input()))

for i in range(H):
    for j in range(W):
        U[j].append(S[i][j])                

for i in range(H):
    T.append(list(input()))

for i in range(H):
    for j in range(W):
        V[j].append(T[i][j])

U.sort()
V.sort()

if U == V:
    print("Yes")
else:
    print("No")
