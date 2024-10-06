n = int(input())
p = [-1]+[int(x) for x in input().split()]

res = 0

i = 1

while i < n:
    if p[i] == i:
        p[i], p[i+1] = p[i+1], p[i]
        res += 1
    i += 1

if p[n] == n:
    res += 1

print(res)
