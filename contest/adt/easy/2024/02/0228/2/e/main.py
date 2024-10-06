N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

matrix = [["." for _ in range(S-R+1)] for _ in range(Q-P+1)]

m1 = max(1-A, 1-B)
M1 = min(N-A, N-B)
m2 = max(1-A, B-N)
M2 = min(N-A, B-1)

for r in range(P, Q+1):
    for c in range(R, S+1):
        dr = r-A
        dc = c-B
        if dr == dc and m1 <= dr and dr <= M1:
            matrix[r-P][c-R] = "#"
        if dr == -dc and m2 <= dr and dr <= M2:
            matrix[r-P][c-R] = "#"

for i in range(Q-P+1):
    print("".join(matrix[i]))
