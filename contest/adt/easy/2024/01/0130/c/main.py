N, M = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

flag = [False for _ in range(N)]
count = 0

for i in range(M):
    for j in range(N):
        if B[i] == A[j] and not flag[j]:
            flag[j] = True
            count += 1
            break
    if count != i+1:
        print("No")
        exit()

print("Yes")
