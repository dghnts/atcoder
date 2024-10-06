from collections import defaultdict
N, Q = map(int,input().split())

A = [int(x) for x in input().split()]

dict = defaultdict(list)

for i in range(N):
    dict[A[i]].append(i+1)
        
#print(dict)
for i in range(Q):
    x,k = map(int, input().split())
    if k < len(dict[x])+1:
        print(dict[x][k-1])
    else:
        print(-1)