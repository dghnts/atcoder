X, A, D, N = map(int, input().split())

m = A
M = A+D*(N-1)

if X <= m or M <= X:
    print(min(abs(X-M), abs(m-X)))
else:
    # Xの値を初項分ずらす
    X -= A
    ans = 0
    ans += X % D
    print(min(ans, D-ans))

'''
if D < 0:
    A = A+D*(N-1)
    D = -D

m = A
M = A+D*(N-1)

if X <= m:
    print(m-X)
elif M <= X:
    print(X-M)
elif D == 0:
    print(0)
else:
    print(min((X-A) % D, D-(X-A) % D))

'''
