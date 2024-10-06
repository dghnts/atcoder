def luca(n: int, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        memo[n] = luca(n-1, memo)+luca(n-2, memo)
        return memo[n]


N = int(input())

print(luca(N))
