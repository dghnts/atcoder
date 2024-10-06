N, K, Q = map(int, input().split())
A = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

for i in range(Q):
    if A[L[i]-1] != N:
        if not A[L[i]-1]+1 in A:
            A[L[i]-1] += 1

print(*A)
