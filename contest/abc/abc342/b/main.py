N = int(input())
P = [int(x) for x in input().split()]

Q = int(input())

for i in range(Q):
    A, B = map(int, input().split())

    if P.index(A) < P.index(B):
        print(A)
    else:
        print(B)
