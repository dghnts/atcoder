import math
N, K = map(int, input().split())

M = math.ceil((math.log2(K)))
# print(M)

ans = 0

for i in range(1, N+1):
    if i >= K:
        ans += 1/N
        continue
    else:
        for j in range(1, M+1):
            if i*(2**j) >= K:
                ans += (1/N) * ((1/2)**j)
                break


print('{:.12f}'.format(ans))
