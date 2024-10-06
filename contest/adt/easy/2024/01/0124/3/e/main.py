N = int(input())
S = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

ans = [0 for i in range(N)]
ans[0] = T[0]

for i in range(N*2):
    ans[(i+1)%N] = min(T[i%N]+S[i%N],T[(i+1)%N])
    T[(i+1)%N] = min(T[i%N]+S[i%N],T[(i+1)%N])

for i in range(N):
    print(ans[i])