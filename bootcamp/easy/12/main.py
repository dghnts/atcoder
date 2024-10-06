K, N = map(int, input().split())
A = [int(x) for x in input().split()]

dist = []

for i in range(N):
    if i != N-1:
        dist.append(A[i+1]-A[i])
    else:
        dist.append(A[0]+K-A[i])

print(K-max(dist))
