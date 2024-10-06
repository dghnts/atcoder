N = int(input())
A = [a for a in input().split()]

A.sort()

print(sum(A[N:2*N]))
