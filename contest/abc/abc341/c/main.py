H, W, N = map(int, input().split())
T = input()
S = []

for i in range(H):
    s = list(input())
    S.append(s)
# print(sorted(list(rand)))
count = 0
for row in range(H):
    # print(row)
    for col in range(W):
        # if (row, col) in sea:
        if S[row][col] == "#":
            continue
        flag = True
        row_copy = row
        col_copy = col
        for t in T:
            if t == "L":
                col_copy -= 1
            elif t == "R":
                col_copy += 1
            elif t == "U":
                row_copy -= 1
            else:
                row_copy += 1
            if S[row_copy][col_copy] == "#":
                flag = False
                break
        if flag:
            count += 1


print(count)
