from collections import defaultdict
N = int(input())

get_money = defaultdict(int)

for i in range(N):
    s = input()
    get_money[s] += 1

M = int(input())

for j in range(M):
    t = input()
    get_money[t] -= 1

ans = 0

for v in get_money.values():
    ans = max(ans, v)
print(ans)
