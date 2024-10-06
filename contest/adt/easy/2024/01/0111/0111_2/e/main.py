N,M  = map(int,input().split())
S = {x:"No" for x in input().split()}
T = [y for y in input().split()]

for t in T:
    S[t] = "Yes"

print(*S.values(), sep="\n")