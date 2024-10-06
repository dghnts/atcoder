from collections import defaultdict

N, M = map(int, input().split())

paths = defaultdict(set)

for i in range(M):
    A,B = map(int,input().split())
    paths[A].add(B)
    paths[B].add(A)

paths = dict(sorted(paths.items()))

for i in range(1,N+1):
    if i not in paths.keys():
        print(0)
    else:
        paths[i] = sorted(list(paths[i]))
        print(len(paths[i]),*paths[i])    