N = int(input())
A = [int(x) for x in input().split()]

length = sum(A)
ans = sum(A)
total = 0
for i in range(N):
    total += A[i]
    ans = min(ans, abs(length-2*total))
print(ans)
