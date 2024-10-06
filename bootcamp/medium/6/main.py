H, W = map(int, input().split())
S = [["." for _ in range(W+2)]]

for row in range(H):
    s = ["."]+list(input())+["."]
    S.append(s)

S.append(["." for _ in range(W+2)])

'''
for i in range(len(S)):
    print("".join(S[i]))
'''

for row in range(1, H+1):
    for col in range(1, W+1):
        if S[row][col] == ".":
            # S[row][col] = 0
            bombs = 0
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if (r != 0 or c != 0):
                        if S[row+r][col+c] == "#":
                            bombs += 1
            S[row][col] = chr(ord('0')+bombs)

for row in range(1, H+1):
    print("".join(S[row][1:-1]))
