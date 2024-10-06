from collections import defaultdict
N, M, T = map(int, input().split())
A = [int(x) for x in input().split()]

bonus_floor  = defaultdict(int)

for i in range(M):
    floor,time = map(int,input().split())
    bonus_floor[floor-1]=time

for i in range(N-1):
    T -= A[i]
    T += bonus_floor[i]
    
    if T <= 0:
        break

if T > 0:
    print("Yes")
else:
    print("No")