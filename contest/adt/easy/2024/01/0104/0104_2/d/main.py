from copy import deepcopy

N = int(input())

A = []

for i in range(N):
    string = list(input())
    string = [int(x) for x in string]
    A.append(string)

B = deepcopy(A)

for i in range(N):
    for j in range(N):
        if i == 0:
            if j == N - 1:
                B[i + 1][j] = str(A[i][j])
            else:
                B[i][j + 1] = str(A[i][j])
        elif i == N - 1:
            if j == 0:
                B[i - 1][j] = str(A[i][j])
            else:
                B[i][j - 1] = str(A[i][j])
        elif j == 0:
            B[i - 1][j] = str(A[i][j])
        elif j == N - 1:
            B[i+1][j] = str(A[i][j])
        else:
            B[i][j] = str(A[i][j])

for i in range(N):
    row = ''.join(B[i])
    print(row)