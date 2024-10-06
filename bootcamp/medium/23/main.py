N, M = map(int, input().split())

num = ["0" for _ in range(N)]
S = []
C = []
for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

num = "".join(num)

for n in range(1, 10**N+1):
    flg = False
    m = len(str(n))
    for i in range(M):
        # print(n//(10**(N-S[i])), i)
        if n//(10**(m-S[i])) % 10 == C[i]:
            flg = True
        else:
            flg = False
            break

    # print(flg)
    if flg:
        print(n)
        exit()

print(-1)
