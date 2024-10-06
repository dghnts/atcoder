N, A, B = map(int, input().split())

for r in range(N):
    ans = ""
    for c in range(N):
        if r%2 == 0:
            if c%2 == 0:
                ans += "."*B
            else:
                ans += "#"*B
        else:
            if c%2 == 1:
                ans += "."*B
            else:
                ans += "#"*B
    for j in range(A):
        print(ans)