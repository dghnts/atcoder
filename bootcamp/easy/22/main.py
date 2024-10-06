N, x = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort()

sum = 0

for i in range(N):
    sum += A[i]
    if sum > x:
        i -= 1
        break
    if i == N-1 and sum != x:
        i -= 1

print(i+1)
