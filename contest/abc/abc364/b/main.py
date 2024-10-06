H, W = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1
map = [[] for _ in range(H)]

for h in range(H):
    map[h] = list(input())

X = input()

for x in X:
    #    print(x)
    if x == "L" and c-1 > -1 and map[r][c-1] == ".":
        c -= 1
    if x == "R" and c+1 < W and map[r][c+1] == ".":
        c += 1
    if x == "U" and r-1 > -1 and map[r-1][c] == ".":
        r -= 1
    if x == "D" and r+1 < H and map[r+1][c] == ".":
        r += 1
#    print(r, c)
r += 1
c += 1
print(r, c)
