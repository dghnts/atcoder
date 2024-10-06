n = int(input())
s = input()

dict = {}
res = 1
for i in range(n):
    if s[i] not in dict.keys():
        dict[s[i]] = 1
    else:
        dict[s[i]] += 1

for v in dict.values():
    res *= v+1

res -= 1

print(res % (10**9+7))
