k, s = map(int, input().split())

res = 0
for x in range(k+1):
    for y in range(k+1):
        if 0 <= s-x-y and s-x-y <= k:
            res += 1

print(res)
