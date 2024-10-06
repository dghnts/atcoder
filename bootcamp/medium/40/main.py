N, M = map(int, input().split())
X = [int(x) for x in input().split()]

X.sort()

dist = []
ans = 0

if N < M:
    for i in range(M-1):
        dist.append(X[i+1]-X[i])

dist.sort()
ans += sum(dist[:M-N])

print(ans)
