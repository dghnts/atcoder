N = int(input())
S = input()
ans = 0
for i in range(N):
    r = set()
    l = set()
    for j in range(N):
        s = S[j]
        if j < i:
            l.add(s)
        else:
            r.add(s)
    ans = max(ans, len(r & l))

print(ans)
