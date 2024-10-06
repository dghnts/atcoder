N = int(input())
score = []
ans = 0

for i in range(N):
    s = int(input())
    if s % 10 != 0:
        score.append(s)
    ans += s
score.sort()

if ans % 10 == 0:
    if len(score) != 0:
        print(ans-score[0])
    else:
        print(0)
else:
    print(ans)
