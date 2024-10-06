S = input()

remove = {"a", "e", "i", "o", "u"}

ans = ""

for s in S:
    if s not in remove:
        ans += s

print(ans)