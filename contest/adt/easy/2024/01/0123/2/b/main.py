N,K = map(int,input().split())
A = [int(x) for x in input().split()]

for i in range(K):
    A =A[1:]
    A.append(0)

print(*A)