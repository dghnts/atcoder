N, X = map(int, input().split())
A = [int(x)-1 for x in input().split()]
X -= 1

flag = [False for _ in range(N)]

flag[X] = True
i = A[X]
ans = 1

while not flag[i]:
    flag[i] = True
    i = A[i]
    ans += 1

print(ans)
