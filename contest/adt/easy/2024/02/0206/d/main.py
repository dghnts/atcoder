H, W = map(int, input().split())
count_box = [0 for _ in range(W)]

for row in range(H):
    for i, v in enumerate(input()):
        if v == "#":
            count_box[i] += 1

print(*count_box)
