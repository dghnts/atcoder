N, A, B = map(int, input().split())

balls = []

if N < A:
    print(N)
elif N < A+B:
    print(A)
else:
    print(N//(A+B)*A+min(N % (A+B), A))
