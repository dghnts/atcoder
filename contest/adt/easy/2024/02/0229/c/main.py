from collections import defaultdict
N = int(input())

A = defaultdict(int)
S = []
T = []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)
    A[s] += 1
    A[t] += 1

for i in range(N):
    if A[S[i]] > 1 and A[T[i]] > 1 and S[i] != T[i]:
        print("No")
        exit()
print("Yes")
