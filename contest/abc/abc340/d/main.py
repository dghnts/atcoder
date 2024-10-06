N = int(input())

# ステージiを遊べるようにするのにかかる時間
dp = [10**9+1 for _ in range(N)]
# ステージ1は0秒で遊べる
dp[0] = 0

for i in range(N-1):
    A, B, X = map(int, input().split())
    dp[i+1] = min(dp[i+1], dp[i]+A)
    dp[X-1] = min(dp[i+1], dp[i]+B)
    print(dp)
print(dp[N-1])
