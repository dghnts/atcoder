S = input()
N = len(S)

dp = [[0 for _ in range(3)] for _ in range(N+1)]

# dpの初期化
dp[0][0] = 0

# i文字目までチェック
for i in range(N+1):
    # i文字目までの分割を考えたときの最後尾の文字列(suffix)を取得
    # i==1,2のときはi文字目までで取得、それ以外は2文字目まで取得
    for j in range(min(i+1, 3)):
        suffix = S[i-j:i]  # i-j文字目からi文字目までのj文字を取得
        # i+1文字目以降のadd文字を取得
        for add in range(1, 3):
            # Nを越えたら終了
            if i + add > N:
                break
            else:
                # print(S[i:i+add+1], suffix)
                if S[i:i+add] != suffix:
                    dp[i+add][add] = max(dp[i+add][add], dp[i][j]+1)
# print(dp)
print(max(dp[N][1], dp[N][2]))
