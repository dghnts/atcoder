from collections import defaultdict
N, Q = map(int, input().split())
A = [int(x) for x in input().split()]

for i in range(Q):
    i, j, k = map(int, input().split())
    if i == 1:
        A[j-1] = k
    else:
        l = j
        r = k
        dict = defaultdict(int)
        for i in range(l-1, r):
            dict[A[i]] += 1
        if len(dict.keys()) == 1:
            print(0)
        else:
            # print(dict.keys())
            print(dict[sorted(dict.keys())[-2]])
