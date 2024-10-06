N, X, Y = map(int, input().split())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)

count_a = 0
count_b = 0

for i in range(N):
    count_a += A[i]
    count_b += B[i]

    if count_a > X or count_b > Y:
        break

print(i+1)
