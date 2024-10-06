N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx_A = 10**6 + 1
mx_B = 10**6 + 1

for i in range(N):
    if A[i] != 0:
        mx_A = min(Q[i] // A[i], mx_A)

k = 10**6+1
ans = 0
for i in range(mx_A + 1):
    for j in range(N):
        if Q[j] - A[j] * i < 0:
            break
        elif B[j] > 0:
            k = min(k,(Q[j] - A[j] * i) // B[j])
    ans = max(ans, k + i)

print(ans)
