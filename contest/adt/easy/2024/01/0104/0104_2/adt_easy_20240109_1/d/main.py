N, W = map(int, input().split())
A = [int(x) for x in input().split()]

flag = [False for _ in range(W+1)]

for i in range(N):
    if A[i] < W + 1:
        flag[A[i]] = True
    for j in range(i + 1, N):
        if A[i] + A[j] < W + 1:
            flag[A[i] + A[j]] = True
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] < W + 1:
                flag[A[i] + A[j] + A[k]] = True

print(sum(flag))
