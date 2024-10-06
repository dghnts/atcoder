n, m = map(int, input().split())

ans = 1

for i in range(1, n+1):
    ans *= i
    ans %= (10**9+7)

for j in range(1, m+1):
    ans *= j
    ans %= (10**9+7)

if abs(n-m) == 1:
    print(ans)
elif n == m:
    print((ans*2) % (10**9+7))
else:
    print(0)
