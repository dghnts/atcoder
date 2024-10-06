from copy import deepcopy

N, Q = map(int, input().split())

head = [1, 0]

parts = [(N - i, 0) for i in range(N)]

move = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

head = [1, 0]
count = 0

for i in range(Q):
    n, m = input().split()
    if n == "1":
        head[0] += move[m][0]
        head[1] += move[m][1]
        parts.append(tuple(head))
    else:
        print(*parts[-int(m)])
