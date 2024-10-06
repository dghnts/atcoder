def repeat(n):
    if n == 1:
        return str(1)
    else:
        return repeat(n-1) + str(n) + repeat(n-1)

N = int(input())

print(*list(repeat(N)))