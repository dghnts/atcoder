N, K = map(int, input().split())
P = [1/2*(int(p)+1) for p in input().split()]

ans = sum(P[:K])
chk = sum(P[:K])

for i in range(K, N):
    chk = chk+P[i]-P[i-K]
    ans = max(ans, chk)

print(ans)
