S = input()
rm = {"a","e","i","o","u"}

ans = ""

for s in S:
    if s not in rm:
        ans += s

print(ans)