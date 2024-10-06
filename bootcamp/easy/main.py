import math


def dist(x: list, y: list):
    N = len(x)
    result = 0
    for i in range(N):
        result += (x[i]-y[i])**2
    return math.sqrt(result)


N, D = map(int, input().split())
X = []

for i in range(N):
    X.append([int(x) for x in input().split()])

ans = 0
for i in range(N):
    for j in range(i+1, N):
        # print(dist(X[i], X[j]))
        if dist(X[i], X[j]).is_integer():
            ans += 1

print(ans)
