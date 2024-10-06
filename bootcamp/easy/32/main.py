N = int(input())
S = input()

x = 0
ans = 0
for i in range(N):
    if S[i] == "I":
        if ans == x:
            ans += 1
        x += 1
    else:
        x -= 1

print(ans)
