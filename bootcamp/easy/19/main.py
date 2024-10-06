N, M, X = map(int, input().split())
A = [int(x)-1 for x in input().split()]

left = 0
right = 0

for i in range(N):
    if i < X and i in A:
        left += 1
    if i >= X and i in A:
        right += 1

print(min(left, right))
