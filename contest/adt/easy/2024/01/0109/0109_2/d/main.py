H, W = map(int, input().split())

board = []

for i in range(H):
    board.append(list(input()))

koma = []

for i in range(H):
    for j in range(W):
        if board[i][j] == "o":
            koma.append((i,j))

ans = 0

for i in range(2):
    ans += abs(koma[0][i]-koma[1][i])

print(ans)