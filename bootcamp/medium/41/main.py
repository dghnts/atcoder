s = input()
n = len(s)

char = {c: 0 for c in set(s)}

for i in range(n):
    char[s[i]] += 1


if len(set(s)) == 1:
    ans = 0
else:
