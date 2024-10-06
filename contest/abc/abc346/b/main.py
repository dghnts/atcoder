W, B = map(int, input().split())

S = "wbwbwwbwbwbw"*20

# print(S)

for i in range(len(S)-W-B):
    w = 0
    b = 0
    for s in S[i:i+W+B]:
        if s == "w":
            w += 1
        else:
            b += 1
    if w == W and b == B:
        print("Yes")
        exit()
print("No")
