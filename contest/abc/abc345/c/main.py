from collections import defaultdict
S = input()
N = len(S)

dic = defaultdict(int)

for s in S:
    dic[s] += 1

ans = 0
# print(dic)
for k, v in dic.items():
    for l, w in dic.items():
        if k != l:
            ans += v*w

ans //= 2

for v in dic.values():
    if v > 1:
        ans += 1
        break
print(ans)
