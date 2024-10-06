N = int(input())
T, A = map(int, input().split())
H = [int(h) for h in input().split()]

temparature = 1000000
ans = 0
for i in range(N):
    if abs(T-H[i]*0.006-A) < temparature:
        temparature = abs(T-H[i]*0.006-A)
        ans = i+1

print(ans)
