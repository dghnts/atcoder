N, M = map(int, input().split())

S = []
C = []

for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)


def ok(string: str):
    global N
    global M
    global S
    global C
    if len(string) != N:
        return False

    for i in range(M):
        if string[S[i]-1] != str(C[i]):
            return False
    return True


def solve():
    for i in range(1001):
        i = str(i)
        if ok(i):
            return i
    return -1


print(solve())
