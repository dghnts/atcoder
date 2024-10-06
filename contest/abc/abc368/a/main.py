N, K = map(int, input().split())

A = [int(x) for x in input().split()]

last_K = A[N-K:]

B = last_K+A[:N-K]

print(*B)
