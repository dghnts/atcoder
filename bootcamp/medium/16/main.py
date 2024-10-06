N = int(input())
score = []
ans = 0

for i in range(N):
    s = int(input())
    if s % 10 != 0:
        score.append(s)
    ans += s
"""
total = sum(score)

if ans % 10 == 0:
    ans = 0

for i in range(N):
    chk_score = total-score[i]
    if chk_score % 10 == 0:
        chk_score = 0

    ans = max(chk_score, ans)

print(ans)
"""

# 別解
