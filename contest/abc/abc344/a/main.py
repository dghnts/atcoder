S = input()

flag = True

ans = ""
for s in S:
    if s == "|":
        flag = not flag
    else:
        if flag:
            ans += s
print(ans)
