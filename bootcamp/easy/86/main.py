S = input()
K = int(input())

for i in range(len(S)):
    if S[i] != "1" and i < K:
        print(S[i])
        exit()
    if i == K-1:
        print(1)
