N = int(input())
A = [0]+[int(a) for a in input().split()]+[0]

res = 0
for i in range(N+1):
    res += abs(A[i+1]-A[i])

for i in range(1, N+1):
    print(res-(abs(A[i]-A[i-1])+abs(A[i+1]-A[i]))+abs(A[i+1]-A[i-1]))
