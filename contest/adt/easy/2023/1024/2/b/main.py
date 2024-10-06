N, M, X, T, D = map(int,input().split())

print( T-D*(X-M) if X > M else T)