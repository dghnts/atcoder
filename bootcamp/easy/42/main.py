from collections import defaultdict
N, M = map(int, input().split())

like = defaultdict(int)

for i in range(N):
    A = list(map(int, input().split()))[1:]
    for a in A:
        like[a] += 1

ans = 0
for v in like.values():
    if v == N:
        ans += 1
print(ans)
