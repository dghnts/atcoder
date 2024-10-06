N = int(input())

good = {}

for i in range(N):
    a, c = map(int, input().split())
    if c not in good.keys():
        good[c] = a
    else:
        good[c] = min(good[c], a)

print(max(good.values()))
