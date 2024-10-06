import math
N, K = map(int, input().split())
A = [int(a) for a in input().split()]

index_1 = A.index(1)

if index_1 == 0 or index_1 == N-1:
    print(math.ceil((N-1)/(K-1)))
else:
    d = (index_1-1) % (K-1)
    left = (index_1+K)//(K-1)
    right = (N-index_1+d)//(K-1)
    print(left+right)
