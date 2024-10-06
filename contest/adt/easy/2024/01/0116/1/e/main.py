N,X = map(int,input().split())

dp = [[0 for _ in range(X+100)] for _ in range(N+1)]

dp[0][0] = 1
for i in range(N):
    a,b = map(int,input().split())
    
    for j in range(X):
        if dp[i][j] == 1:
            dp[i+1][j+a] = 1
            dp[i+1][j+b] = 1

if dp[N][X] == 1:
    print("Yes")
else:
    print("No")