N = int(input())
score = []
for i in range(N):
    score.append(int(input()))

S = sum(score)

dp = [False for _ in range(S+1)]

dp[0] = True
score.sort()
for i in range(N):
    for j in range(S, -1, -1):
        if dp[j] and j+score[i] < S+1:
            dp[j+score[i]] = True

# print(dp)
for i in range(S, -1, -1):
    if dp[i] and i % 10 != 0:
        print(i)
        exit()
print(0)
