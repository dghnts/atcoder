N, M = map(int, input().split())
A = [int(x) for x in input().split()]

connects = []

conn = set()

count = 0

if M == 0:
    print(*[i+1 for i in range(N)])
    exit()

for i in range(N):
    conn.add(i+1)
    if A[count] == i+1:
        conn.add(i+2)
        if count < M-1:
            count += 1
    else:
        connects.append(list(conn))
        conn = set()

ans = []
for conn in connects:
    ans.extend(sorted(conn, reverse=True))

print(*ans)
