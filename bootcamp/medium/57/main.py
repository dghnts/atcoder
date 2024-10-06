n = int(input())

S = dict()

for i in range(n):
    s = list(input())
    s.sort()
    s = "".join(s)
    if s in S.keys():
        S[s] += 1
    else:
        S[s] = 1

ans = 0

for v in S.values():
    ans += v*(v-1)//2

print(ans)
