N = int(input())
A = [int(x) for x in input().split()]

rotate = 0

cut = []

for i in range(N):
    rotate += A[i] % 360
    cut.append()