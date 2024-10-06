N = int(input())
S = input()
C = [int(c) for c in input().split()]

same = []
counts = []
count = 0
for i in range(N):
    if S[i] == S[i+1]:
        same.append(i)
        count += 1
    count.append(count)

# i+1文字目まで確認したときにかかる最小コスト
dp = [0 for _ in range(N)]

dp[0] = C[0]
for i in range(1, N):
    if count[i] == 1:
        dp[i] = 0
    elif i not in same:

        dp[i] = dp[i-1]+

print(dp)
