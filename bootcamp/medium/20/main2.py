N = int(input())

A = []

for i in range(N):
    A.append(int(input()))

A.sort()

ans = set()
count = 1

# print(A)

for i in range(1, N):
    # print(count)
    if A[i-1] == A[i]:
        count += 1
    else:
        if count % 2 != 0:
            ans.add(A[i-1])
        count = 1

print(len(ans))
