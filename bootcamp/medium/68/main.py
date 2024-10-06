h, w = map(int, input().split())

board = [["."]*(w+2)]
point = 0

for i in range(h):
    row = ["."]+list(input())+["."]
    board.append(row)
    point += row.count("#")

board.append(["."]*(w+2))

x = 1
y = 1

flg = True

while True:
    # print(y, x, point)
    if board[y][x] == "#":
        point -= 1
    if x == w and y == h:
        break
    if board[y+1][x] == "#" and board[y][x+1] == "#":
        flg = False
        break
    elif board[y+1][x] == "#":
        y += 1
    elif board[y][x+1] == "#":
        x += 1
    else:
        flg = False
        break
if point != 0:
    flg = False
# print(point)

print("Possible" if flg else "Impossible")
