n, a, b, c, d = map(int, input().split())
s = list(input())

sunuke = a
funuke = b

flg = True

if c < d:
    for i in range(b, d-2):
        if s[i] == "#" and s[i+1] == "#":
            flg = False
            break
    for j in range(a, c-2):
        if s[j] == "#" and s[j+1] == "#":
            flg = False
            break
else:
    for i in range(b-1, d):
        if s[i-1] == "." and s[i] == "." and s[i+1] == ".":
            flg = True
            break
        else:
            flg = False
print("Yes" if flg else "No")
