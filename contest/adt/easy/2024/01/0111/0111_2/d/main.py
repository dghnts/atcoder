N,X = map(int,input().split())
A = sorted([int(x) for x in input().split()])

m = A[0]
M = A[-1]

sigma = sum(A[1:-1])

diff = X-sigma 
if diff <= m:
    ans = 0
elif diff <= M:
    ans = diff
else:
    ans = -1
    
print(ans)