board = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    board[i] = list(map(int, input().split()))

for r1 in range(3):
    for r2 in range(r1, 3):
        for c1 in range(3):
            for c2 in range(c1, 3):
                if board[r1][c1]-board[r2][c1] != board[r1][c2]-board[r2][c2]:
                    print("No")
                    exit()
            for c2 in range(c1, 3):
                if board[r1][c1]-board[r1][c2] != board[r2][c1]-board[r2][c2]:
                    print("No")
                    exit()
print("Yes")
