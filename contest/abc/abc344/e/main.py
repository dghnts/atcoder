N = int(input())
A = {i: int(x) for i, x in enumerate(input().split())}
Q = int(input())

for i in range(Q):
    query = list(map(int, input().split()))
    x = query[1]
    for k in A.keys():
        if A[k] == x:
            break
    if query[0] == 1:
        y = query[2]
        N += 1
        # print(A.keys())
        for j in range(N-1, k+1, -1):
            A[j] = A[j-1]
        A[k+1] = y
    else:
        for j in range(k, N-1):
            A[j] = A[j+1]
        del A[N-1]
        N -= 1
    # print(A.values())
print(*A.values())
