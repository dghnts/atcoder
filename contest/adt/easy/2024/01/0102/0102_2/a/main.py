import itertools

S = list(input())

ans = set()
for p in itertools.permutations(S, len(S)):
    ans.add(p)

print(len(ans))
