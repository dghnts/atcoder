S = input()
n = len(S)

ans = 0

for i in range(n):
    if S[i] == "U":
        ans += n-i-1+i*2
    else:
        ans += i+(n-i-1)*2
print(ans)
