S = input()

ans = ""

for s in S[::-1]:
    if s != ".":
        ans += s
    else:
        break
print(ans[::-1])
