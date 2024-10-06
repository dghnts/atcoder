N, D = map(int, input().split())

flag = [True for _ in range(D)]

for i in range(N):
    S = input()
    for j in range(D):
        if S[j] == "x":
            flag[j] = False
# print(flag)

ans = 0
count = 0

for f in flag:
    if f:
        count += 1
        ans = max(count, ans)
    else:
        ans = max(count, ans)
        count = 0

print(ans)
