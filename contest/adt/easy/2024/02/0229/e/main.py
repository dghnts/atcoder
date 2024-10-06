from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int, input().split()))

char = defaultdict(list)

for i in range(N):
    char[A[i]].append(i+1)

for i in range(Q):
    x, k = map(int, input().split())
    if k < len(char[x])+1:
        print(char[x][k-1])
    else:
        print(-1)
