n = int(input())
a = list(map(int, input().split()))

sunuke = a[0]
araiguma = sum(a[1:])

res = abs(sunuke-araiguma)

for i in range(1, n-1):
    sunuke += a[i]
    araiguma -= a[i]
    res = min(res, abs(sunuke-araiguma))

print(res)
