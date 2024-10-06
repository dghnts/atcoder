n = int(input())
s = []

chars = {chr(i): 51 for i in range(ord("a"), ord("z")+1)}

for i in range(n):
    s.append(input())

for i in range(n):
    for k in chars.keys():
        chars[k] = min(chars[k], s[i].count(k))

res = ""

for k, v in chars.items():
    res += k*v

print(res)
