S = input()
N = len(S)

seq = [0 for _ in range(N+1)]

for i in range(N):
    if S[i] == "<":
        seq[i+1] = max(seq[i+1], seq[i]+1)

for j in range(N-1, -1, -1):
    if S[j] == ">":
        seq[j] = max(seq[j], seq[j+1]+1)
    # print(seq)
# print(seq)
print(sum(seq))
