def gcd(a, b):
    if a < b:
        a, b = b, a
    """
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b
    """
    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return a*b//g


n = int(input())

t = []

for i in range(n):
    t.append(int(input()))


res = t[0]

for i in range(n):
    #    print(res, t[i])
    res = lcm(res, t[i])

print(res)
