N = int(input())
A = [int(x) for x in input().split()]
A.sort(reverse=True)

Alice = 0
Bob = 0
for i in range(N):
    if i % 2 == 0:
        Alice += A[i]
    else:
        Bob += A[i]
print(abs(Alice-Bob))
