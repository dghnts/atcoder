# 現在地から移動可能なルートを探:q
索する


def route(board, x, y):
    if route[y][x] == "T":
        return True
    route[y][x] = "#"
    for next_x, next_y for ([[x, y-1], [x+1, y], [x, y+1], [x-1, y]]):
        if route[next_y][route_x] == "#":
            continue
        route +=


h, w = map(int, input().split())
board = [["#"]*(w+2)]

for i in range(h):
    rows = ["#"]+list(input())+["#"]
    board.append(rows)
    if "S" in rows:
        row = i+1
        col = rows.index("S")

board.append(["#"]*(w+2))


n = int(input())
drag = [[None for _ in range(w+2)] for _ in range(h+2)]

for i in range(n):
    r, c, e = map(int, input().split())
    drag[r][c] = e

# 通過したことがある場所かを確認するboard
chk_board = [[False for _ in range(w+2)] for _ in range(h+2)]

chk_board[row][col] = True
flg = False
energy = 0

route = [[row, col]]

if drag[row][col] != None:
    energy = drag[row][col]
    counta = 0
    # 移動が可能な限り繰り返す
    while True:
        if board[row][col] == "T":
            flg = True
            break
        board[row][col] = "#"
        for next in [[row-1, col], [row, col+1], [row+1, col], [row, col-1]]:
            if board[next[0]][next[1]] == "#":
                continue
            row = next[0]
            col = next[1]
            route.append([row, col])
        print(route)
if flg:
    print("Yes")
else:
    print("No")
