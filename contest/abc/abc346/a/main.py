N = int(input())
A = [int(a) for a in input().split()]

B = []
for i in range(N-1):
    B.append(A[i]*A[i+1])

print(*B)
