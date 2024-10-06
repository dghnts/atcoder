N = int(input())
X = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
Q = int(input())
people = {X[i]: P[i] for i in range(N)}

s = {}

for i in range(N):
    if i == 0:
        s[X[i]] = P[i]
    else:
        s[X[i]] = s[X[i-1]]+P[i]

# print(s)
for i in range(Q):
    L, R = map(int, input().split())
    if L == R:
        if L not in s.keys():
            print(0)
            continue
        else:
            print(s[L])
            continue

    if L not in s.keys():
        for i in range(N):
            if X[i] - L > 0:
                L = X[i]
                break

    if R not in s.keys():
        for i in range(N-1, -1, -1):
            if R - X[i] > 0:
                R = X[i]
                break

    print(s[R]-s[L]+people[L])
