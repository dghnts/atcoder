N = int(input())
A = [int(x) for x in input().split()]

called = [True for _ in range(N)]

for i in range(N):
    if called[i]:
        called[A[i]-1] = False

ans = [i+1 for i in range(N) if called[i]]

print(len(ans))
print(*ans)