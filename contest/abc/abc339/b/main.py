H, W, N = map(int, input().split())

'''
# upper:0,right:1,below:2,left:3
direction = 0

colors = [["." for _ in range(W)] for _ in range(H)]

row = 0
col = 0

for i in range(N):
    # print(colors[row][col])
    if colors[row][col] == ".":
        colors[row][col] = "#"
        direction = (direction+1) % 4
    else:
        colors[row][col] = "."
        direction = (direction-1) % 4
    # print(colors[row][col])
    if direction == 0:
        row = (row-1) % H
    elif direction == 1:
        col = (col+1) % W
    elif direction == 2:
        row = (row+1) % H
    else:
        col = (col-1) % W
    # print(row, col, direction)
    # print(colors[row][col])
    # for i in range(H):
    #    print("".join(colors[i]))
for i in range(H):
    print("".join(colors[i]))

'''

## 別解##

colors = [["." for _ in range(W)] for _ in range(H)]
row = 0
col = 0

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
direction = 0

for i in range(N):
    if colors[row][col] == ".":
        colors[row][col] = "#"
        direction += 1
    else:
        colors[row][col] = "."
        direction -= 1
    direction %= 4

    row += drow[direction]
    col += dcol[direction]
    row %= H
    col %= W

for row in range(H):
    print("".join(colors[row]))
