S = input()
N = len(S)

B = "0"

for i in range(N):
    if B[-1] == "0":
        B += "1"
    else:
        B += "0"

ans = 0
for i in range(N):
    ans += abs(int(S[i])-int(B[i]))

print(min(N-ans, ans))
