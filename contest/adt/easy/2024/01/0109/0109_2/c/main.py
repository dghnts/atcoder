from collections import defaultdict

N = int(input())
S = defaultdict(int)

for i in range(N):
    S[input()] += 1

S = sorted(S.items(), key=lambda x: x[1], reverse=True)

print(S[0][0])