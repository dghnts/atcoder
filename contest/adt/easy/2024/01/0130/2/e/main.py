square = []

porn = []
for i in range(9):
    square.append(list(input()))
    for j in range(9):
        if square[-1][j] == "#":
            porn.append((i, j))
