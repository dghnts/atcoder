W, H, x, y = map(int, input().split())

pat = 0

if x == W/2 and y == H/2:
    pat = 1

print(W*H/2, pat)
