n = int(input())

A = []
B = []

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A = A[::-1]
B = B[::-1]

res = 0

for i in range(n):
    A[i] += res
    # print(A[i])
    if A[i] % B[i] != 0:
        res += B[i]-(A[i] % B[i])

print(res)
