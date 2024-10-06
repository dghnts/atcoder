H, W = map(int, input().split())
S = [[0 for _ in range(H)] for _ in range(W)]
T = [[0 for _ in range(H)] for _ in range(W)]

for i in range(2*H):
    row = list(input())
    row = [1 if v == "#" else 0 for v in row]
    if i < H:
        for j in range(W):
            S[j][i] = row[j]
    else:
        for j in range(W):
            T[j][i-H] = row[j]

S.sort()
T.sort()

# print(S)
# print(T)
if S == T:
    print("Yes")
else:
    print("No")
