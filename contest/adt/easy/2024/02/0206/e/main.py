N, M = map(int, input().split())
A = sorted([int(x) for x in input().split()], reverse=True)
B = sorted([int(x) for x in input().split()], reverse=True)
C = sorted(list(set(A+B)))

X = 0
countA = 0
countB = M
for c in C:
    if c in A:
        countA = N-A.index(c)-1
    if c in B:
        countB = B.index(c)
    if countA >= countB:
        X = c
print(X)
