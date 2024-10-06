N, K = map(int, input().split())
A = [int(a) for a in input().split()]

ans = []
for a in A:
    if a % K == 0:
        ans.append(a//K)

print(*ans)
