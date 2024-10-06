R,C = map(int,input().split())

A= []

for i in range(2):
    A.append([int(x) for x in input().split()])

print(A[R-1][C-1])