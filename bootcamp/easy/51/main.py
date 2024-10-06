N, A, B = map(int, input().split())

ans = 0

for i in range(1, N+1):
    S = 0
    j = i
    while True:
        if j == 0:
            if A <= S and S <= B:
                ans += i
            break
        S += j % 10
        j //= 10

print(ans)
