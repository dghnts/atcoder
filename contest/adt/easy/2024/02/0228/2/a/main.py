N = int(input())
A = [int(x) for x in input().split()]

ans = []
for i in range(N):
    ans.append(sum(A[7*i:7*(i+1)]))

print(*ans)
