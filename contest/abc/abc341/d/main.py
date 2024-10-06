import math
N, M, K = map(int, input().split())

if M < N:
    N, M = M, N

G = math.gcd(N, M)

N //= G
M //= G

n = N
m = M

# このとき,gcd(N,M)=1
rep = n + m - 2

K -= 1
ans = (n*m) * (K // rep)

K %= rep

for i in range(K):
    if n < m:
        n += N
    else:
        m += M
ans += min(n, m)
print(ans*G)
