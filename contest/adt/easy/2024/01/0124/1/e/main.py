from copy import deepcopy
from collections import defaultdict

N = int(input())
S = input()

mx = defaultdict(int)

l = 0

while l < N:
    r = l+1
    while r < N and S[l]==S[r]: r += 1
    mx[S[l]] = max(mx[S[l]], r-l)
    l = deepcopy(r)

print(sum(mx.values()))