N = int(input())
A = [int(x) for x in input().split()]

ans = [0 for _ in range(2 * N + 1)]

for i, a in enumerate(A):
    ans[2 * i + 1] = ans[a - 1] + 1
    ans[2 * i + 2] = ans[a - 1] + 1

print(*ans, sep="\n")
