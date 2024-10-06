A, B, C, X, Y = map(int, input().split())

ans = 0
common = min(X, Y)
if A+B < 2*C:
    ans += (A+B)*common
else:
    ans += 2*C*common

# print(ans)
X -= common
Y -= common

# print(A*X+B*Y, 2*C*max(X, Y))
ans += min(A*X+B*Y, 2*C*max(X, Y))

print(ans)
