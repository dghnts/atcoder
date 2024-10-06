N, K = map(int, input().split())

trees = []

for i in range(N):
    trees.append(int(input()))

trees.sort()

ans = 10**9
for i in range(N-K+1):
    ans = min(ans, trees[i+K-1]-trees[i])
print(ans)
