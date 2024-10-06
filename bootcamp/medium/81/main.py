s = input()
n = len(s)

res = 0

for i in range(1, n):
    if s[i-1] != s[i]:
        res += 1

print(res)
