A, B = map(int, input().split())

ans = 0
for n in range(A, B+1):
    n = list(str(n))
    m = n[::-1]
    if n == m:
        ans += 1
print(ans)
