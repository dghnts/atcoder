N, M, C = map(int, input().split())
B = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    A = [int(x) for x in input().split()]
    chk = C
    for j in range(M):
        chk += A[j]*B[j]
    if chk > 0:
        ans += 1
print(ans)
