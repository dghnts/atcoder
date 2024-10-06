s = input()
n = len(s)

ans = ""

for i in range(n):
    if s[i] != "B":
        ans = ans+s[i]
    else:
        if ans != "":
            ans = ans[:-1]

print(ans)
