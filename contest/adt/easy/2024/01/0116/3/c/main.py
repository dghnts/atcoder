L, R = map(int, input().split())
S = list(input())

ans = ""
rev = S[L - 1 : R][::-1]

cnt = 0
for i in range(len(S)):
    if i < L - 1 or R - 1 < i:
        ans += S[i]
    else:
        ans += rev[cnt]
        cnt += 1

print(ans)
