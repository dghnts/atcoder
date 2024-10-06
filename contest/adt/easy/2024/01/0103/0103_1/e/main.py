N = int(input())
S = list(input())

count = 0

for i in range(N):
    if count % 2 == 0:
        if S[i] ==",":
            S[i] = "."
    if S[i] == "\"":
        count += 1

S = "".join(S)
print(S)