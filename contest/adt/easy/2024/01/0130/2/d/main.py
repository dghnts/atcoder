N = int(input())

square = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    A, B, C, D = map(int, input().split())
    for i in range(A, B):
        for j in range(C, D):
            square[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        ans += square[i][j]
print(ans)
