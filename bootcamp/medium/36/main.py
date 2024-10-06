import math

N, X = map(int, input().split())
city = [int(x) for x in input().split()]

ans = float("inf")

ans = abs(X-city[0])

for i in range(1, N):
    ans = math.gcd(ans, X-city[i])

print(ans)
