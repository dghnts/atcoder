N = int(input())
K = int(input())
x = [int(x) for x in input().split()]

ans = 0

for i in range(N):
    ans += min(x[i], K-x[i])

print(ans*2)
