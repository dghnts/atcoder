N = int(input())
X = [int(x) for x in input().split()]

p = sum(X) / N

ans = 0

"""
q = sum(X)//N

if abs(q-p) > abs(q+1-p):
    P = q+1
else:
    P = q
"""
P = round(p)

for i in range(N):
    ans += (X[i] - P) ** 2

print(ans)
