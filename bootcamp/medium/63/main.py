w, h, n = map(int, input().split())

square = [["W" for _ in range(w)] for _ in range(h)]

black_pannel = 0

for i in range(n):
    x, y, a = map(int, input().split())

    if a == 1:
        for i in range(h):
            for j in range(x):
                if square[i][j] != "B":
                    black_pannel += 1
                    square[i][j] = "B"
    elif a == 2:
        for i in range(h):
            for j in range(x, w):
                if square[i][j] != "B":
                    black_pannel += 1
                    square[i][j] = "B"
    elif a == 3:
        for i in range(y):
            for j in range(w):
                if square[i][j] != "B":
                    black_pannel += 1
                    square[i][j] = "B"
    else:
        for i in range(y, h):
            for j in range(w):
                if square[i][j] != "B":
                    black_pannel += 1
                    square[i][j] = "B"

# for i in range(h):
#    print(*square[i])
print(h*w-black_pannel)
