N = int(input())
P = [int(x) for x in input().split()]

ans = 0

for i in range(N):
    if P[0] == P[i] and i != 0:
        ans = max(ans,1)
    elif P[0] < P[i]:
        ans = max(ans, P[i]-P[0]+1)
print(ans)
