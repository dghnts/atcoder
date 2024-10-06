S = input()

ans = ""

N = len(S)

for i in range(N//2):
    ans += S[2*i+1]
    ans += S[2*i]

print(ans)
