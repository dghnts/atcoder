N = int(input())
A = []

for i in range(2):
    A.append([int(x) for x in input().split()])

dp = [[0 for _ in range(N)] for _ in range(2)]

# dp[0][0] = A[0][0]

for i in range(N):
    dp[0][i] = dp[0][i-1]+A[0][i]

for j in range(N):
    dp[1][j] = max(dp[0][j]+A[1][j], dp[1][j-1]+A[1][j])

print(dp[1][N-1])
