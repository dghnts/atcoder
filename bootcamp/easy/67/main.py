from collections import defaultdict
N = int(input())

dict = defaultdict(int)

for i in range(N):
    dict[input()] += 1

M = max(dict.values())

ans = []

for k, v in dict.items():
    if v == M:
        ans.append(k)

ans.sort()

for v in ans:
    print(v)
