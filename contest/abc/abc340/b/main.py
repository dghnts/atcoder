A = []
Q = int(input())

for i in range(Q):
    n, x = map(int, input().split())
    if n == 1:
        A.append(x)
    else:
        print(A[-x])
