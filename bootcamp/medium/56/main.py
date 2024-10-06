n, k, s = map(int, input().split())

if s < 10**9:
    ans = [s]*k
    ans += [s+1]*(n-k)
else:
    ans = [s]*k
    ans += [1]*(n-k)

print(*ans)
