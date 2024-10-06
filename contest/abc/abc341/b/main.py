N = int(input())
A = [int(x) for x in input().split()]

for i in range(N-1):
    s, t = map(int, input().split())
    # print(s, t)
    # print(A[i]//s, t, t)
    A[i+1] += t*(A[i] // s)
    # print(A)

print(A[N-1])
