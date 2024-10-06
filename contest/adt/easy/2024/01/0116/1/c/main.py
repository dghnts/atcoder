import string
H,W = map(int,input().split())

A = []

Uppercase = string.ascii_uppercase

for i in range(H):
    A.append(list(map(int,input().split())))

S = [["" for _ in range(W)] for _ in range(H)]
for r in range(H):
    for c in range(W):
        if A[r][c] == 0:
            S[r][c] = "."
        else:
            S[r][c] = Uppercase[A[r][c]-1]

for r in range(H):
    print("".join(S[r]))