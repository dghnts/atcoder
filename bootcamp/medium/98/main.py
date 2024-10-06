def prime_factorize(n):
    p = 2
    res = {}
    if n <= 3:
        res[n] = 1

    while p*p <= n:
        while n % p == 0:
            n //= p
            if p not in res.keys():
                res[p] = 1
            else:
                res[p] += 1
        p += 1
    if n != 1:
        res[n] = 1

    return res


n, p = map(int, input().split())

ans = 1

for k, v in prime_factorize(p).items():
    ans *= max(1, k**(v//n))

print(ans)
