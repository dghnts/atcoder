A, B, K = map(int, input().split())

fast_K = A+K
back_K = B-K
for i in range(A, B+1):
    if i < fast_K or back_K < i:
        print(i)
