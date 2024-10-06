N = int(input())
B = [float('inf')]+[int(b) for b in input().split()]+[float('inf')]

A = [0 for _ in range(N)]

for i in range(N):
    A[i] = min(B[i], B[i+1])

print(sum(A))
