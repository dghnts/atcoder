N = int(input())
A = [int(x) for x in input().split()]

# Nが偶数の時
if N % 2 == 0:
    if A[N//2] > A[N//2+1]:
        A = A[:-1]
    else:
        A = A[1:]
    N -= 1

if A[N // 2] > N // 2 + 1:
    A[N // 2] = N // 2 + 1

right = A[: N // 2]
left = A[N // 2 + 1 :]
count = 0

right_count = 0
left_count = 0
for i in range(N//2):
    if right[i] > i:
        right_count += 1

for j in range(N//2):
    if left[-1-j] > j:
        left_count += 1

count = min(right_count,left_count)

print(count+1)
