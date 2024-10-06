N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ans = sum(A)

for i in range(N):
    defeat = min(A[i], B[i])
    A[i] -= defeat
    if A[i] == 0:
        A[i+1] = max(0, A[i+1]-B[i]+defeat)

print(ans-sum(A))
