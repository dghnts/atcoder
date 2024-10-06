N = int(input())
'''
H = [0]+[int(h) for h in input().split()]

dp = [0 for _ in range(N+1)]

for i in range(N-1, 0, -1):
    if H[i] >= H[i+1]:
        dp[i] = dp[i+1]+1

print(max(dp))
'''

H = [int(h) for h in input().split()]
ans = 0
x = 0
i = 0
while True:
    if i == N-1:
        break
    if H[i] >= H[i+1]:
        x += 1
        i += 1
    else:
        x = 0
        i += 1
    ans = max(ans, x)
print(ans)
